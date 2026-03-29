#!/bin/bash
pytest --alluredir=allure-results --clean-alluredir -v
allure serve allure-results
