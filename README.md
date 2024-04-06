# Employee Management System Dashboard

Designed for those who like modern UI elements and beautiful websites. Made of hundred of elements, designed blocks and fully coded pages, EMS Dashboard is ready to help you manage your office in a seamless way.

We created many examples for pages like Sign In, Profile and so on.

**Fully Coded Elements**

EMS Dashboard is built with over 70 frontend individual elements, like buttons, inputs, navbars, navtabs, cards or alerts, giving you the freedom of choosing and combining. All components can take variations in colour, that you can easily modify using Chakra's style props.

## Quick Start

- Clone the repo.
- `cd 15_Intelligent_Automation`
- `cd material-react-app`
- `npm install`
- `npm start`

## Login

If a user is not logged in can access only the authentication pages: Login, Register and Forgot Password. By default, there **admin@jsonapi.com** with password **secret** as credentials.
For authentication context and protected routes were used to keep track of the state of the users. Axios together with an http service and helped by an auth service and crud service handled the requests. The **/src/service** keeps the logic of the services while **/src/context** has the logic for the different contexts used, including the authentication context.

In the **/src/auth/login/index.js** is the logic for logging in an existing user:

```
    try {
      const response = await AuthService.login(myData);
      authContext.login(response.access_token, response.refresh_token);
    } catch (res) {
      if (res.hasOwnProperty("message")) {
        setCredentialsError(res.message);
      } else {
        setCredentialsError(res.errors[0].detail);
      }
    }
```

## Register

It can be added a new user by registration. The user has a name, email, password and role that needs to be added. All the inputs are verified and validated. You can simply access the page with the **Sign up** button or adding **/register** in the url.

In the **/src/auth/register/index.js** is the logic for signing up a new user:

```
    const response = await AuthService.register(myData);

    authContext.login(response.access_token, response.refresh_token);
```

## Forgot Password

In case of forgetting its password, the user can go to a page where he adds the email of the account and an email will be send to that address to help with resetting the password. It can be accessed from the Login page by clicking the **here** button or by adding **/forgot-password**.

In the **/src/auth/forgot-password/index.js** is the logic for requesting a password reset:

```
    try {
      const response = await authService.forgotPassword(myData);
      if (error === false) {
        setNotification(true);
      }
    } catch (err) {
      console.error(err);
      return null;
    }
```

## Reset Password

For resetting the password, the user must acceess the url sent int the email. By adding the new password and the confirmation and then pressing the **channge** button the data of the account is updated. You can go back to login from the button in notification.

In the **/src/auth/reset-password/index.js** is the logic for resetting the password:

```
  useEffect(() => {
    // get the token and email sent in the url
    const queryParams = new URLSearchParams(window.location.search);
    setToken(queryParams.get("token"));
    setEmail(queryParams.get("email"));
  }, []);
```

## User Profile

From the sidenav, in the CRUDs section, or by adding **/cruds/user-profile** in the url, the User Profile is a dynamic page where the user can add details about him: profile image, name, email or change password. Validation is added for every input.

In the **/src/services/auth-serivce** you can find the routes sets for the request and in the **/src/cruds/user-profile** is the component for the editing the profile details.

```
  getProfile = async() => {
    const getProfile = 'me';
    return await HttpService.get(getProfile);
  }

  updateProfile = async (newInfo) => {
    const updateProfile = "me";
    return await HttpService.patch(updateProfile, newInfo);
  }
```

### What's included

You'll find the following directories and files:

```
./src
├── App.js
├── assets
│   ├── images
│   │   ├── apple-icon.png
│   │   ├── bg-profile.jpeg
│   │   ├── bg-reset-cover.jpeg
│   │   ├── bg-sign-in-basic.jpeg
│   │   ├── bg-sign-up-cover.jpeg
│   │   ├── bruce-mars.jpg
│   │   ├── favicon.png
│   │   ├── home-decor-1.jpg
│   │   ├── home-decor-2.jpg
│   │   ├── home-decor-3.jpg
│   │   ├── home-decor-4.jpeg
│   │   ├── icons
│   │   │   └── flags
│   │   │       ├── AU.png
│   │   │       ├── BR.png
│   │   │       ├── DE.png
│   │   │       ├── GB.png
│   │   │       └── US.png
│   │   ├── illustrations
│   │   │   └── pattern-tree.svg
│   │   ├── ivana-square.jpg
│   │   ├── kal-visuals-square.jpg
│   │   ├── logo-ct-dark.png
│   │   ├── logo-ct.png
│   │   ├── logos
│   │   │   ├── gray-logos
│   │   │   │   ├── logo-coinbase.svg
│   │   │   │   ├── logo-nasa.svg
│   │   │   │   ├── logo-netflix.svg
│   │   │   │   ├── logo-pinterest.svg
│   │   │   │   ├── logo-spotify.svg
│   │   │   │   └── logo-vodafone.svg
│   │   │   ├── mastercard.png
│   │   │   └── visa.png
│   │   ├── marie.jpg
│   │   ├── small-logos
│   │   │   ├── bootstrap.svg
│   │   │   ├── creative-tim.svg
│   │   │   ├── devto.svg
│   │   │   ├── github.svg
│   │   │   ├── google-webdev.svg
│   │   │   ├── icon-bulb.svg
│   │   │   ├── logo-asana.svg
│   │   │   ├── logo-atlassian.svg
│   │   │   ├── logo-invision.svg
│   │   │   ├── logo-jira.svg
│   │   │   ├── logo-slack.svg
│   │   │   ├── logo-spotify.svg
│   │   │   └── logo-xd.svg
│   │   ├── team-1.jpg
│   │   ├── team-2.jpg
│   │   ├── team-3.jpg
│   │   ├── team-4.jpg
│   │   └── team-5.jpg
│   ├── theme
│   │   ├── base
│   │   │   ├── borders.js
│   │   │   ├── boxShadows.js
│   │   │   ├── breakpoints.js
│   │   │   ├── colors.js
│   │   │   ├── globals.js
│   │   │   └── typography.js
│   │   ├── components
│   │   │   ├── appBar.js
│   │   │   ├── avatar.js
│   │   │   ├── breadcrumbs.js
│   │   │   ├── button
│   │   │   │   ├── contained.js
│   │   │   │   ├── index.js
│   │   │   │   ├── outlined.js
│   │   │   │   ├── root.js
│   │   │   │   └── text.js
│   │   │   ├── buttonBase.js
│   │   │   ├── card
│   │   │   │   ├── cardContent.js
│   │   │   │   ├── cardMedia.js
│   │   │   │   └── index.js
│   │   │   ├── container.js
│   │   │   ├── dialog
│   │   │   │   ├── dialogActions.js
│   │   │   │   ├── dialogContent.js
│   │   │   │   ├── dialogContentText.js
│   │   │   │   ├── dialogTitle.js
│   │   │   │   └── index.js
│   │   │   ├── divider.js
│   │   │   ├── flatpickr.js
│   │   │   ├── form
│   │   │   │   ├── autocomplete.js
│   │   │   │   ├── checkbox.js
│   │   │   │   ├── formControlLabel.js
│   │   │   │   ├── formLabel.js
│   │   │   │   ├── input.js
│   │   │   │   ├── inputLabel.js
│   │   │   │   ├── inputOutlined.js
│   │   │   │   ├── radio.js
│   │   │   │   ├── select.js
│   │   │   │   ├── switchButton.js
│   │   │   │   └── textField.js
│   │   │   ├── iconButton.js
│   │   │   ├── icon.js
│   │   │   ├── linearProgress.js
│   │   │   ├── link.js
│   │   │   ├── list
│   │   │   │   ├── index.js
│   │   │   │   ├── listItem.js
│   │   │   │   └── listItemText.js
│   │   │   ├── menu
│   │   │   │   ├── index.js
│   │   │   │   └── menuItem.js
│   │   │   ├── popover.js
│   │   │   ├── sidenav.js
│   │   │   ├── slider.js
│   │   │   ├── stepper
│   │   │   │   ├── index.js
│   │   │   │   ├── stepConnector.js
│   │   │   │   ├── stepIcon.js
│   │   │   │   ├── step.js
│   │   │   │   └── stepLabel.js
│   │   │   ├── svgIcon.js
│   │   │   ├── table
│   │   │   │   ├── tableCell.js
│   │   │   │   ├── tableContainer.js
│   │   │   │   └── tableHead.js
│   │   │   ├── tabs
│   │   │   │   ├── index.js
│   │   │   │   └── tab.js
│   │   │   └── tooltip.js
│   │   ├── functions
│   │   │   ├── boxShadow.js
│   │   │   ├── gradientChartLine.js
│   │   │   ├── hexToRgb.js
│   │   │   ├── linearGradient.js
│   │   │   ├── pxToRem.js
│   │   │   └── rgba.js
│   │   ├── index.js
│   │   └── theme-rtl.js
│   └── theme-dark
│       ├── base
│       │   ├── borders.js
│       │   ├── boxShadows.js
│       │   ├── breakpoints.js
│       │   ├── colors.js
│       │   ├── globals.js
│       │   └── typography.js
│       ├── components
│       │   ├── appBar.js
│       │   ├── avatar.js
│       │   ├── breadcrumbs.js
│       │   ├── button
│       │   │   ├── contained.js
│       │   │   ├── index.js
│       │   │   ├── outlined.js
│       │   │   ├── root.js
│       │   │   └── text.js
│       │   ├── buttonBase.js
│       │   ├── card
│       │   │   ├── cardContent.js
│       │   │   ├── cardMedia.js
│       │   │   └── index.js
│       │   ├── container.js
│       │   ├── dialog
│       │   │   ├── dialogActions.js
│       │   │   ├── dialogContent.js
│       │   │   ├── dialogContentText.js
│       │   │   ├── dialogTitle.js
│       │   │   └── index.js
│       │   ├── divider.js
│       │   ├── form
│       │   │   ├── autocomplete.js
│       │   │   ├── checkbox.js
│       │   │   ├── formControlLabel.js
│       │   │   ├── formLabel.js
│       │   │   ├── input.js
│       │   │   ├── inputLabel.js
│       │   │   ├── inputOutlined.js
│       │   │   ├── radio.js
│       │   │   ├── select.js
│       │   │   ├── switchButton.js
│       │   │   └── textField.js
│       │   ├── iconButton.js
│       │   ├── icon.js
│       │   ├── linearProgress.js
│       │   ├── link.js
│       │   ├── list
│       │   │   ├── index.js
│       │   │   ├── listItem.js
│       │   │   └── listItemText.js
│       │   ├── menu
│       │   │   ├── index.js
│       │   │   └── menuItem.js
│       │   ├── popover.js
│       │   ├── sidenav.js
│       │   ├── slider.js
│       │   ├── stepper
│       │   │   ├── index.js
│       │   │   ├── stepConnector.js
│       │   │   ├── stepIcon.js
│       │   │   ├── step.js
│       │   │   └── stepLabel.js
│       │   ├── svgIcon.js
│       │   ├── table
│       │   │   ├── tableCell.js
│       │   │   ├── tableContainer.js
│       │   │   └── tableHead.js
│       │   ├── tabs
│       │   │   ├── index.js
│       │   │   └── tab.js
│       │   └── tooltip.js
│       ├── functions
│       │   ├── boxShadow.js
│       │   ├── gradientChartLine.js
│       │   ├── hexToRgb.js
│       │   ├── linearGradient.js
│       │   ├── pxToRem.js
│       │   └── rgba.js
│       ├── index.js
│       └── theme-rtl.js
├── auth
│   ├── forgot-password
│   │   └── index.js
│   ├── login
│   │   └── index.js
│   ├── register
│   │   └── index.js
│   └── reset-password
│       └── index.js
├── components
│   ├── MDAlert
│   │   ├── index.js
│   │   ├── MDAlertCloseIcon.js
│   │   └── MDAlertRoot.js
│   ├── MDAvatar
│   │   ├── index.js
│   │   └── MDAvatarRoot.js
│   ├── MDBadge
│   │   ├── index.js
│   │   └── MDBadgeRoot.js
│   ├── MDBox
│   │   ├── index.js
│   │   └── MDBoxRoot.js
│   ├── MDButton
│   │   ├── index.js
│   │   └── MDButtonRoot.js
│   ├── MDInput
│   │   ├── index.js
│   │   └── MDInputRoot.js
│   ├── MDPagination
│   │   ├── index.js
│   │   └── MDPaginationItemRoot.js
│   ├── MDProgress
│   │   ├── index.js
│   │   └── MDProgressRoot.js
│   ├── MDSnackbar
│   │   ├── index.js
│   │   └── MDSnackbarIconRoot.js
│   └── MDTypography
│       ├── index.js
│       └── MDTypographyRoot.js
├── context
│   └── index.js
├── examples
│   ├── Breadcrumbs
│   │   └── index.js
│   ├── Cards
│   │   ├── BlogCards
│   │   │   └── SimpleBlogCard
│   │   │       └── index.js
│   │   ├── InfoCards
│   │   │   ├── DefaultInfoCard
│   │   │   │   └── index.js
│   │   │   └── ProfileInfoCard
│   │   │       └── index.js
│   │   ├── MasterCard
│   │   │   └── index.js
│   │   ├── ProjectCards
│   │   │   └── DefaultProjectCard
│   │   │       └── index.js
│   │   └── StatisticsCards
│   │       └── ComplexStatisticsCard
│   │           └── index.js
│   ├── Charts
│   │   ├── BarCharts
│   │   │   ├── HorizontalBarChart
│   │   │   │   ├── configs
│   │   │   │   │   └── index.js
│   │   │   │   └── index.js
│   │   │   ├── ReportsBarChart
│   │   │   │   ├── configs
│   │   │   │   │   └── index.js
│   │   │   │   └── index.js
│   │   │   └── VerticalBarChart
│   │   │       ├── configs
│   │   │       │   └── index.js
│   │   │       └── index.js
│   │   ├── BubbleChart
│   │   │   ├── configs
│   │   │   │   └── index.js
│   │   │   └── index.js
│   │   ├── DoughnutCharts
│   │   │   └── DefaultDoughnutChart
│   │   │       ├── configs
│   │   │       │   └── index.js
│   │   │       └── index.js
│   │   ├── LineCharts
│   │   │   ├── DefaultLineChart
│   │   │   │   ├── configs
│   │   │   │   │   └── index.js
│   │   │   │   └── index.js
│   │   │   ├── GradientLineChart
│   │   │   │   ├── configs
│   │   │   │   │   └── index.js
│   │   │   │   └── index.js
│   │   │   ├── ProgressLineChart
│   │   │   │   ├── config
│   │   │   │   │   └── index.js
│   │   │   │   └── index.js
│   │   │   └── ReportsLineChart
│   │   │       ├── configs
│   │   │       │   └── index.js
│   │   │       └── index.js
│   │   ├── MixedChart
│   │   │   ├── configs
│   │   │   │   └── index.js
│   │   │   └── index.js
│   │   ├── PieChart
│   │   │   ├── configs
│   │   │   │   └── index.js
│   │   │   └── index.js
│   │   ├── PolarChart
│   │   │   ├── configs
│   │   │   │   └── index.js
│   │   │   └── index.js
│   │   └── RadarChart
│   │       ├── configs
│   │       │   └── index.js
│   │       └── index.js
│   ├── Configurator
│   │   ├── ConfiguratorRoot.js
│   │   └── index.js
│   ├── Footer
│   │   └── index.js
│   ├── Items
│   │   └── NotificationItem
│   │       ├── index.js
│   │       └── styles.js
│   ├── LayoutContainers
│   │   ├── DashboardLayout
│   │   │   └── index.js
│   │   └── PageLayout
│   │       └── index.js
│   ├── Lists
│   │   └── ProfilesList
│   │       └── index.js
│   ├── Navbars
│   │   ├── DashboardNavbar
│   │   │   ├── index.js
│   │   │   └── styles.js
│   │   └── DefaultNavbar
│   │       ├── DefaultNavbarLink.js
│   │       ├── DefaultNavbarMobile.js
│   │       └── index.js
│   ├── ProtectedRoute
│   │   └── index.js
│   ├── Sidenav
│   │   ├── index.js
│   │   ├── SidenavCollapse.js
│   │   ├── SidenavRoot.js
│   │   └── styles
│   │       ├── sidenavCollapse.js
│   │       └── sidenav.js
│   ├── Tables
│   │   └── DataTable
│   │       ├── DataTableBodyCell.js
│   │       ├── DataTableHeadCell.js
│   │       └── index.js
│   └── Timeline
│       ├── context
│       │   └── index.js
│       ├── TimelineItem
│       │   ├── index.js
│       │   └── styles.js
│       └── TimelineList
│           └── index.js
├── index.js
├── layouts
│   ├── authentication
│   │   ├── components
│   │   │   ├── BasicLayout
│   │   │   │   └── index.js
│   │   │   ├── CoverLayout
│   │   │   │   └── index.js
│   │   │   └── Footer
│   │   │       └── index.js
│   │   ├── reset-password
│   │   │   └── cover
│   │   │       └── index.js
│   │   ├── sign-in
│   │   │   └── index.js
│   │   └── sign-up
│   │       └── index.js
│   ├── billing
│   │   ├── components
│   │   │   ├── Bill
│   │   │   │   └── index.js
│   │   │   ├── BillingInformation
│   │   │   │   └── index.js
│   │   │   ├── Invoice
│   │   │   │   └── index.js
│   │   │   ├── Invoices
│   │   │   │   └── index.js
│   │   │   ├── PaymentMethod
│   │   │   │   └── index.js
│   │   │   ├── Transaction
│   │   │   │   └── index.js
│   │   │   └── Transactions
│   │   │       └── index.js
│   │   └── index.js
│   ├── dashboard
│   │   ├── components
│   │   │   ├── OrdersOverview
│   │   │   │   └── index.js
│   │   │   └── Projects
│   │   │       ├── data
│   │   │       │   └── index.js
│   │   │       └── index.js
│   │   ├── data
│   │   │   ├── reportsBarChartData.js
│   │   │   └── reportsLineChartData.js
│   │   └── index.js
│   ├── notifications
│   │   └── index.js
│   ├── profile
│   │   ├── components
│   │   │   ├── Header
│   │   │   │   └── index.js
│   │   │   └── PlatformSettings
│   │   │       └── index.js
│   │   ├── data
│   │   │   └── profilesListData.js
│   │   └── index.js
│   ├── rtl
│   │   ├── components
│   │   │   ├── OrdersOverview
│   │   │   │   └── index.js
│   │   │   └── Projects
│   │   │       ├── data
│   │   │       │   └── index.js
│   │   │       └── index.js
│   │   ├── data
│   │   │   ├── reportsBarChartData.js
│   │   │   └── reportsLineChartData.js
│   │   └── index.js
│   ├── tables
│   │   ├── data
│   │   │   ├── authorsTableData.js
│   │   │   └── projectsTableData.js
│   │   └── index.js
│   ├── user-management
│   │   ├── data.js
│   │   └── index.js
│   └── user-profile
│       ├── Header
│       │   └── index.js
│       ├── index.js
│       └── PlatformSettings
│           └── index.js
├── routes.js
└── services
    ├── auth-service.js
    ├── htttp.service.js
    └── interceptor.js
```

## Browser Support

At present, we officially aim to support the last two versions of the following browsers:

<img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/chrome.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/firefox.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/edge.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/safari.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/opera.png" width="64" height="64">
