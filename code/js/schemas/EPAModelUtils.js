const fs = require('fs'); 
const sleep = require('util').promisify(setTimeout);
const axios = require('axios');
const axiosRetry = require('axios-retry');


const buildEPASchema = (ModelUrl, OutputFileName) => {

  let schema = {};

  // let schemaTablesFields = require('./schemaTablesFields.json');

  // The EPA website is very inconsistent with it's urls across databases.  We're
  // trying to pull schema info for SDWIS, RadNet and Tri databases so these REGEXs 
  // are designed to be able to support all three.
  const tableUrlRegex = new RegExp(/<area.*?href="(.*?)".*?>/g);
  const tableNameRegex = new RegExp(/p_table_name=(.*?)&/);
  
  // Regex that finds the table description on a table page
  const tableDescRegex = new RegExp(/(?:<b>Description:<\/b>\r?\n?)([\s\S]*?)(?:[<br>]?<b>Columns:<\/b>)/);

  // Regex that finds the Url for a field on a EPA table page
  const fieldUrlRegex = new RegExp(/\"(\/\/ofmpub\.epa\.gov\/enviro\/EF_METADATA_HTML(?:.*?_page\?)p_column_name\=(.+?(?=&|")).*?)"/g);
  
  // Regex that finds the field description on a field page
  const fieldDescRegex = new RegExp(/(?:<b>Description:\s?<\/b>\r?\n?)([\s\S]*?)(?:[<br>]?<b>Envirofacts Table Name\(s\):<\/b>)/);

  // Regex that finds the unordered list that contains the properties for a field on a field page
  const propsULRegex = new RegExp(/<b>Properties:<\/b><ul>([\s\S]*?)<\/ul>/);
  // Regex that splits out the property names and values from the props unordered list
  const propRegex = new RegExp(/<b>(.+?):<\/b>\s?(.*?)\s?<\/li>/g);

  // Removes some white space from 
  const replaceWhitespace = new RegExp(/[\s:]/g);

  // Checks if a url is protocal relative or not
  const protocolRegex = new RegExp(/^(?:\/\/)/);

  // Strips out BRs from tale and field descriptions
  const replaceBR = new RegExp(/<br\s*[\/]?>/gi);


  /**
   * Urls in the EPA website can have two issues:
   * 1) Escaped ampersands '&amp;' will not work in our axios calls, so we replace
   *    with '&'
   * 
   * 2) Protocol-relative urls work in the browser, but not in our node/axios calls.
   *    So we add https if protocol doesn't exist.
   *    //ofmpub.epa.gov/enviro/... becomes https://ofmpub.epa.gov/enviro/...
   * @function
   * @name cleanUrl
   * @param {string} url - The Url to be cleaned up.
   * @return {string} Cleaned url
   */
  const cleanUrl = (url) => {
    url = url.replace('&amp;', '&');
    return protocolRegex.test(url) ? 'https:' + url : url;
  }


  /**
   * Replace BRs in text with space and trims spaces from ends.
   * @function
   * @name cleanDescription
   * @param {string} description - The string to be cleaned.  Used here for cleaning up table and field descriptions.
   * @return {string} Cleaned string
   */
  const cleanDescription = (description) => {
    return description.replace(replaceBR, ' ').trim();
  }


  /**
   * Requests a web page using axios.get()
   * @function
   * @name getPage
   * @param {url} url - Url of the page get
   * @return {string} content of the requested page
   */
  const getPage = async (url) => {
    let cleanedUrl = cleanUrl(url);
    // console.log('getPage() url, cleanedUrl', url, cleanedUrl);
    axiosRetry(
      axios,
      {
        retries: 3,
        retryDelay: (retryCount) => {
          return retryCount * 2000;
        }
      }
    );

    return axios.get(cleanedUrl)
      .then(async response => {
        await sleep(500);
        if (response.status === 200) {
          return response.data;
        }
      },
      error => {
        console.log(error);
        return null;
      }
    );
  }


  /**
   * Function that retrieves the main model page for an EPA database containing table information
   * @function
   * @name getSchemaTables
   * @param {string} modelUrl - Content of the web page
   * @return {Object} Object containing the table names as keys along with the table's url and a property of each table object
   */
  const getSchemaTables = async (modelUrl) => {
    const schemaTables = {};
    const response = await getPage(modelUrl);

    for (let match; (match = tableUrlRegex.exec(response)) !== null;) {
      let url = match[1];
      let tableName = tableNameRegex.exec(url)[1];

      schemaTables[tableName] = {
        url: cleanUrl(url),
        description: '',
        fields: {}
      };
    }
    return schemaTables;
  }


  /**
   * Function that parses the content of and EPA web page containing field information
   * for an database table
   * @function
   * @name getFieldInfo
   * @param {string} pageContent - Content of the web page
   * @return {Object} Object containing the field description, url, and properties
   */
  const getFieldInfo = (pageContent) => {
    // console.log(pageContent);
    let fieldInfo = {};
    let fieldParse = fieldDescRegex.exec(pageContent);
    // Most fields in an EPA database have some metadata about the field.  Some do not.  
    // This message is displayed on the page when there's none, so we'll reuse it.
    fieldInfo.description = fieldParse !== null ? cleanDescription(fieldParse[1]) : 'Metadata no available for this column';
    fieldInfo.props = {};
  
    let propsParse = propsULRegex.exec(pageContent)
    // pageContent.match(propsULRegex);
    // console.log('propsParse', propsParse);
    let propLIs = propsParse !== null ? propsParse[1] : '';
  
    let match;
    while ((match = propRegex.exec(propLIs)) !== null) {
      if ( match ) {
        let propName = match[1];
        let propValue = match[2].trim();
        fieldInfo.props[propName] = propValue;
      }
    }
    return fieldInfo;
  }

  
  /**
   * Function that parses the content of EPA web page containing table information
   * for a database model
   * @function
   * @name getFieldInfo
   * @param {string} pageContent - Content of the web page
   * @return {Object} Object containing the field description, url, and properties
   */
  const getTableInfo = (pageContent) => {
    let tableInfo = {};
    let tableParse = tableDescRegex.exec(pageContent);
    let description = tableParse !== null ? cleanDescription(tableParse[1]) : '';

    tableInfo.description = description;
    tableInfo.fields = {};
    
    for (let match; (match = fieldUrlRegex.exec(pageContent)) !== null;) {
      // console.log('match[0], match[1]', match[0], match[1], match[2])
      let url = match[1];
      let fieldName = match[2];
      tableInfo.fields[fieldName] = {
        url,
        props: {}
      };
    }
    return tableInfo;
  }


  const tableInfoGenerator = async function* () { //added async
    // The database table names are stored as keys in the schema object
    let tableNames = Object.keys(schema).sort();

    /**
     *  Loop over each table and create an object containing name, url, description, and fields
     * This will be passed back in our yield and merged with the schema object using destructuring
     * so it should be returned in the form of 
     * {
     *   tableName: tableInfoObj
     * }
     */
    for (let i=0; i<tableNames.length; i++) {
      let tableName = tableNames[i];
      console.log('tableName', tableName);
 
      let tableUrl = schema[tableName].url;

      let tableInfoObj = {
        url: tableUrl,
        description: '',
        fields: {}
      };

      // Get the content of the page for this table from the EPA website
      let tablePageContent = await getPage(tableUrl);
      let tableInfo = getTableInfo(tablePageContent);
      // console.log('tableInfo', tableInfo);

      tableInfoObj.description = tableInfo.description;
      let fieldNames = Object.keys(tableInfo.fields);
      // console.log('fieldNames', fieldNames);
      
      for await (fieldName of fieldNames) {
        console.log('fieldName', fieldName);

        let fieldUrl = cleanUrl(tableInfo.fields[fieldName].url);
        console.log('fieldUrl', fieldUrl);

        let fieldPageContent = await getPage(fieldUrl);
        let fieldInfo = getFieldInfo(fieldPageContent);
        // console.log('fieldInfo', fieldInfo);
        
        tableInfoObj.fields[fieldName] = {
          url:         fieldUrl,
          description: fieldInfo.description,
          props:       { ...fieldInfo.props }
        };
      }
      
      // console.log(tableName, tableInfoObj);
      yield { [ tableName ]: tableInfoObj }
    }
  }


  /** 
   * IMPORTANT: This code requires using the --harmony_generators flag from the CLI
   *   node --harmony_generators someJSFileCallingBuildSchema
   * 
   * If we use simple async loop over tables and within that an async loop over each 
   * field in the table, node bombs out with too many nested async axios get calls.  
   * So intead we'll syncronously loop over each table using an async generator so 
   * each set of async calls will resolve before moving on to the next table.
  */
  const buildSchema = async (startUrl, fileName) => {
    const schemaTables = await getSchemaTables(startUrl);
    schema = schemaTables;
    
    const tables = tableInfoGenerator();
    
    //use 'for await...of' instead of 'for...of'
    for await (const tableInfo of tables) {
      // console.log('buildSchema() tableInfo', tableInfo);
      schema = {
        ...schema,
        ...tableInfo
      };
      fs.writeFileSync(
        `${__dirname}/${fileName}`,
        JSON.stringify(schema),
        'utf8'
      );
    }
  
  }

  buildSchema(ModelUrl, OutputFileName);
};

module.exports = { buildEPASchema };
