"use strict"

const {logger} = require('./logger')
const axios = require('axios')
const fs = require('fs')
const path = require("path")

const db = require('./database').Database.getInstance()

class RAIN {
    constructor() {
        this.database = db
    }
    static getInstance() {
        if (!!!this.instance) {
            this.instance = new RAIN()
        }
        return this.instance
    }
    getForecast() {
        return this.database.getEverything()
    }
    hasPredictedData(data) {
        logger.info("Predicted Data Received")
        this.database.insertPredictedData(data)
        logger.info("Predicted Data Complete")
    }
}

module.exports = {
    RAIN
}