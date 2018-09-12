const sleep = require('util').promisify(setTimeout);
const axios = require('axios');
const fs = require('fs'); 

const startUrl = 'https://www.epa.gov/enviro/sdwis-model';



// const tableNameRegex = new RegExp('<h1>\nTable Name: (.*)\n</h1>');
let schema = {};

const tableUrlRegex = new RegExp(/<a href=\"https:\/\/iaspub\.epa\.gov\/enviro\/ef_metadata_html\.ef_metadata_table\?p_table_name=(.*)\&amp;p_topic=SDWIS\" target=\"_blank\">/g);
const tableHrefRegex = new RegExp(/<a href=\"(.*)\" target=\"_blank\">/);
const tableDescRegex = new RegExp(/(?:<b>Description:<\/b>\r?\n?)([\s\S]*?)(?:[<br>]?<b>Columns:<\/b>)/);

const fieldUrlRegex = new RegExp(/<a href=\"\/\/ofmpub.epa.gov\/enviro\/EF_METADATA_HTML.sdwis_page\?p_column_name=(.*)\">/g);
const fieldHrefRegex = new RegExp(/<a href=\"(.*)\">/);
const fieldDescRegex = new RegExp(/(?:<b>Description:\s?<\/b>\r?\n?)([\s\S]*?)(?:[<br>]?<b>Envirofacts Table Name\(s\):<\/b>)/);

const propsULRegex = new RegExp(/<b>Properties:<\/b><ul>([\s\S]*?)<\/ul>/);
const propRegex = new RegExp(/<b>(.+?)<\/b>(.+?)<\/li>/g);

const replaceWhitespace = new RegExp(/[\s:]/g);
const protocolRegex = new RegExp(/^(?:\/\/)/);
const replaceBR = new RegExp(/<br\s*[\/]?>/gi);


const cleanUrl = (url) => {
  url = url.replace('&amp;', '&');
  // Some of the URLs are protocal relative ////ofmpub.epa.gov/enviro/... instead of https://ofmpub.epa.gov/enviro/...
  return protocolRegex.test(url) ? 'https:' + url : url;
}

const cleanDescription = (description) => {
  // Replace BRs in text with space and trim from ends.
  return description.replace(replaceBR, ' ').trim();
}

const getPage = async (url) => {
  return axios.get(cleanUrl(url))
    .then(async response => {
      await sleep(2000);
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

getFieldInfo = async (url) => {
  let fieldInfo = {
    props: {}
  };
  sleep()
  let response = await getPage(url);
 
  fieldInfo.description = cleanDescription(fieldDescRegex.exec(response)[1]);
  
  let propLIs = (response.match(propsULRegex)[1]).replace(replaceWhitespace, '');
  let match;
  while ((match = propRegex.exec(propLIs)) !== null) {
    fieldInfo.props[match[1]] = match[2];
  }
  return  fieldInfo;
}
// getFieldInfo('//ofmpub.epa.gov/enviro/EF_METADATA_HTML.sdwis_page?p_column_name=ENFORCEMENT_ACTION_TYPE_CODE');

getTableInfo = async (url) => {
  let tableInfo = {};
  let response = await getPage(url);

  tableInfo.description = cleanDescription(tableDescRegex.exec(response)[1]);

  for (let match; (match = fieldUrlRegex.exec(response)) !== null;) {
    url = fieldHrefRegex.exec(match[0])[1];
    let fieldInfo = getFieldInfo(url);
    tableInfo[match[1]] = {
      url: url,
      props: fieldInfo.props
    };
  }
  return tableInfo;
}
// getTableInfo('https://iaspub.epa.gov/enviro/ef_metadata_html.ef_metadata_table?p_table_name=ENFORCEMENT_ACTION&p_topic=SDWIS');

getSchemaTables = async () => {
  await getPage(startUrl).then(response => {
    for (let match; (match = tableUrlRegex.exec(response)) !== null;) {
      let url = tableHrefRegex.exec(match[0])[1];
      let tableInfo = getTableInfo(url);
      schema[match[1]] = {
        url,
        description: tableInfo.description,
        fields: tableInfo.fields
      };
    }
  }).then(() => {
    console.log(schema);
    let writable = fs.createWriteStream(__dirname + '/schema.json');
    writable.write(JSON.stringify(schema));
  });
}

getSchemaTables();

