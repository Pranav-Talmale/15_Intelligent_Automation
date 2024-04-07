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
import React from 'react';
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
      <MDButton variant="gradient" color="dark">
        <Icon sx={{ fontWeight: "bold" }}>add</Icon>
        &nbsp;add new card
      </MDButton>
    </MDBox>
    <MDBox p={2}>
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <MDBox
            borderRadius="lg"
            display="flex"
            justifyContent="space-between"
            alignItems="center"
            p={3}
            sx={{
              border: ({ borders: { borderWidth, borderColor } }) =>
                `${borderWidth[1]} solid ${borderColor}`,
            }}
          >
            {/* <MDBox component="img" src={masterCardLogo} alt="master card" width="10%" mr={2} /> */}

            <MDBox
              ml="auto"
              lineHeight={0}
              color={darkMode ? "white" : "dark"}
            >
              <Tooltip title="Generate" placement="top">
                <Icon sx={{ cursor: "pointer" }} fontSize="small">
                  search
                </Icon>
              </Tooltip>
            </MDBox>
          </MDBox>
        </Grid>
      </Grid>
    </MDBox>
  </Card>
);
}
 

export default AIChatbox;





