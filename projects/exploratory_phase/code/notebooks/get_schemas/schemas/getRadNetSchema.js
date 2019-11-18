const { buildEPASchema } = require('./EPAModelUtils');

const EPAModelUrl = 'https://www.epa.gov/enviro/radnet-model';
const OutputFileName = 'RadNet_schema.json';

/** 
 * This file reaches out to the EPA's website and pulls the web pages for the
 * tables and fields related to a particular database model.  This file creates 
 * a json file containing information about the structure of the EPA's RadNet
 * database.
 * 
 * IMPORTANT: buildSchema() uses for await with a generator function which requires 
 * the use of the --harmony_generators flag to run.  So this file should be run from 
 * the CLI using the following command:
 * 
 * node --harmony_generators getRadNetSchema.js
 */
buildEPASchema(EPAModelUrl, OutputFileName);
