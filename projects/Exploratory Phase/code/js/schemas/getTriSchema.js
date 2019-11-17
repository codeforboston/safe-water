const { buildEPASchema } = require('./EPAModelUtils');

const TriSubjectAreas = [
  {
    name: 'TRI Facility Identification',
    url:  'https://www.epa.gov/enviro/tri-facility-identification-subject-area-model'
  },
  {
    name: 'TRI Reported Chemical Information',
    url:  'https://www.epa.gov/enviro/tri-reported-chemical-information-subject-area-model'
  },
  {
    name: 'TRI Releases to Environmental Media',
    url:  'https://www.epa.gov/enviro/tri-releases-environmental-media-subject-area-model'
  },
  {
    name: 'TRI Transfers of Wastes to Off-Site Locations',
    url:  'https://www.epa.gov/enviro/tri-transfers-wastes-site-locations-subject-area-model'
  },
  {
    name: 'TRI Onsite Treatment, Energy Recovery and Recycling Methods',
    url:  'https://www.epa.gov/enviro/tri-onsite-treatment-energy-recovery-and-recycling-methods-subject-area-model'
  },
  {
    name: 'TRI Source Reduction and Recycling Activities',
    url:  'https://www.epa.gov/enviro/tri-source-reduction-and-recycling-activities-subject-area-model'
  },
  {
    name: 'TRI References',
    url:  'https://www.epa.gov/enviro/tri-references-subject-area-model'
  },
  {
    name: 'TRI Form R Schedule 1',
    url:  'https://www.epa.gov/enviro/tri-form-r-schedule-1-subject-area-model'
  }
];

// IMPORTANT: In the interest of time, I didn't build a generator function for this. 
// Currently this is just run separately for each subject area of the Tri database.
let i = 7;
let EPAModelUrl = TriSubjectAreas[i].url;
let OutputFileName = TriSubjectAreas[i].name.replace(/\s/g, '_') + '.json';
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
