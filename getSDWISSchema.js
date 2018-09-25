const { buildEPASchema } = require('./EPAModelUtils');

const EPAModelUrl = 'https://www.epa.gov/enviro/sdwis-model';
const OutputFileName = 'SDWIS_schema.json';

/** 
 * This file reaches out to the EPA's website and pulls the web pages for the
 * tables and fields related to a particular database model.  This file creates 
 * a json file containing information about the structure of the EPA's Safe 
 * Drinking Water Information System (SDWIS) database.
 * 
 * IMPORTANT: buildSchema() uses for await with a generator function which requires 
 * the use of the --harmony_generators flag to run.  So this file should be run from 
 * the CLI using the following command:
 * 
 * node --harmony_generators getSDWISSchema.js
 */
buildEPASchema(EPAModelUrl, OutputFileName);
