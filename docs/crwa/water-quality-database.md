# EPA Water Quality Database

The CRWA submits data to the [EPA's water quality database](https://www.epa.gov/waterdata/water-quality-data-wqx).

## What's in the data?

The Safe Water Act requires various local, state, and federal agencies to monitor lakes, streams, rivers and other of bodies of water for their quality.

## Formatting and uploading the data

The CRWA's data is formatted differently than what is required for the EPA's Water Quality Database. You can find more information about this process in the "Upload Data" tab of the Water Quality Data page on the EPA's website.

At the moment, we are currently working through the EPA's documentation, which is very long. Part of our needs for the data modernization task is to learn more about the process that the EPA requires, and summarize it.

### Ways to submit data

There are three ways to submit data to the Water Quality database:

**Via Excel template.** (What CRWA does.) The WQX Web Template Dictionary is available [here](https://www.epa.gov/waterdata/water-quality-exchange-web-template-files). Each one of the templates comes with a very old Excel file and a PDF explaining how to use the Excel template.

**Via XML.** An organization can also submit XML files through the EPA's Central Data Exchange (CDX). It's hard to make sense of what's going on here; we should invest some time into trying to understand what this process is.

**Via the Water Quality Exchange (WQX) API.** More info on this is available [here](https://cdx.epa.gov/WQXWeb/StaticPages/WebServicesGuide.htm), which I found [here](https://www.epa.gov/waterdata/wqx-web-application-programming-interface). Note that this is not mentioned in the "Upload Data" tab of the WQX page. Users need to register for an API key through the WQX Web application. According to the documentation, "Data is submitted by sending an HTTP GET/POST to the URI with appropriate parameters supplied. The minimum parameters for every request include the UserID, Timestamp, and Signature, which includes the name of the method being invoked." This is probably what we will end up building a tool for.