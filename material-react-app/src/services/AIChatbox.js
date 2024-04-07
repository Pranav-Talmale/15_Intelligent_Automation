// AIChatbox.js

import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";

import MDBox from "components/MDBox";
import MDInput from "components/MDInput";
import MDTypography from "components/MDTypography";
import Card from "@mui/material/Card";
import Grid from "@mui/material/Grid";
import Icon from "@mui/material/Icon";
import Tooltip from "@mui/material/Tooltip";
import React from "react";
import MDButton from "components/MDButton";
import { useMaterialUIController } from "context";
const AIChatbox = () => {
  // Chatbox logic goes here
  const [controller] = useMaterialUIController();
  const { darkMode } = controller;
  return (
    <Card id="delete-account">
      <MDBox
        pt={2}
        px={2}
        display="flex"
        justifyContent="space-between"
        alignItems="center"
      >
        <MDTypography variant="h6" fontWeight="medium">
          AI CHATBOT
        </MDTypography>
      </MDBox>
      <MDBox p={30}m={30}>
        <Grid  justifyContent="center">
          <Grid item xs={12} md={6} ml={0}>
            <MDBox
              borderRadius="lg"
              display="flex-start"
              justifyContent="center"
              alignItems="center"
              p={2}
              sx={{
                border: ({ borders: { borderWidth, borderColor } }) =>
                  `${borderWidth[1]} solid ${borderColor}`,
              }}
            >
              
              {/* <MDBox component="img" src={masterCardLogo} alt="master card" width="10%" mr={2} /> */}

              <MDBox ml="15" 
                lineHeight={0}
                color={darkMode ? "white" : "dark"}
              >
                <Tooltip title="Generate" placement="top">
                  {/* <Icon sx={{ cursor: "pointer" }} fontSize="small">
                    search
                  </Icon> */}
                  <MDButton variant="gradient" color="dark">
                &nbsp;Submit
              </MDButton>
                </Tooltip>
              </MDBox>
            </MDBox>
          </Grid>
        </Grid>
      </MDBox>
    </Card>
  );
};

export default AIChatbox;
