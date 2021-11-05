# EMS-MIBEL-RESTrade

There are five components inside the EMS-MIBEL-RESTrade Spine ToolBox project:

- **Mibel Day-ahead Input** contains the input of the **Run EMS** component. The schema that validates this input is available at ./MarketRunner/resources/generalSchema.json.
- **Run EMS** executes the MIBEL day-ahead market (defined in the input of the previous component), validating it with the JSON schema available at <https://em.gecad.isep.ipp.pt/api/v1/mibel/schema>.
- **Filter Player Result** filters the result of the market session executed in the previous component to a predefined player, passed as an argument.
- **Print Player Result JSON** prints the result of the player selected in the previous tool in JSON format.
- **Export Player Result Excel** exports the result of the player selected in the previous tool to an XLSX file.
