<h1 align="center">
  <a name="logo"><img src="https://github.com/CS-UCR/final-project-stockoverflow/blob/master/frontend/src/assets/logo.svg" width="400"></a>
  <br>
  KirbyUpB
</h1>

Team Members: Aditya Acharya, Eric Ong, Ji Hwan Kim, John Shin, Neal Goyal

## Table of Contents
- [Overview](#overview)
- [Usage](#usage)
- [How To Run](#how-to-run)
- [Diagrams](#diagrams)
- [Dependencies](#dependencies)

## Overview
Welcome to Stock Overflow. Stock Overflow is a full-stack web application that uses news data to predict changes in stock prices. Not only does it show the prediction, but it also retrieves the news articles that are most relevant to that stock and provides the most impactful keywords associated to the price of the stock of the day.

User Actions: 
- Entering Stock Info
- Search
- Resizing stock chart
- Clicking article

Four Types of Users: Active Investors, Passive Investors, Speculators, Stock Analysts. 

1. As an **active investor**, I want to be able to read relevant articles affecting the current stock price, so that I can make well-researched investment decisions and view stock performance. 
2. As a **passive investor**, I want to view historical data on stocks in a chart, so that I can make low-risk, calculated investments. 
3. As a **speculator**, I want to see relevant terms affecting stocks, so that I can make quick buy/sell investment decisions.
4. As a **stock analyst**, I want to view daily trends on stocks, so that I can make accurate investments for my clients.


## Usage
Demo: https://www.youtube.com/watch?v=YMJh-efLch4

![Image](https://github.com/CS-UCR/final-project-stockoverflow/blob/master/backend/Screen%20Shot%202019-12-11%20at%202.49.15%20AM.png)

## How To Run
In the project directory, you can run:

### `npm start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (Webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Diagrams

Sequence Diagram
![Image](https://github.com/CS-UCR/final-project-stockoverflow/blob/master/backend/Screen%20Shot%202019-12-11%20at%202.32.12%20AM.png)

Frontend Structure
![Image](https://github.com/CS-UCR/final-project-stockoverflow/blob/master/backend/Screen%20Shot%202019-12-11%20at%202.32.25%20AM.png)

Overall System Diagram
![Image](https://github.com/CS-UCR/final-project-stockoverflow/blob/master/backend/Screen%20Shot%202019-12-11%20at%202.33.55%20AM.png)


## Dependencies
Install Node Package Manager (npm). [Helpful Documentation](https://www.npmjs.com/get-npm)
