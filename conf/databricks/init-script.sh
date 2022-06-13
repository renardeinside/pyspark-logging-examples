#!/bin/bash
echo "Executing on Driver: $DB_IS_DRIVER"
if [[ $DB_IS_DRIVER = "TRUE" ]]; then
    echo "Setting the log4j configuration on the driver"
    SOURCE_LOG4J_PATH="/dbfs/logs-config/driver-log4j.properties"
    DRIVER_LOG4J_PATH="/home/ubuntu/databricks/spark/dbconf/log4j/driver/log4j.properties"
    cat SOURCE_LOG4J_PATH >> DRIVER_LOG4J_PATH
    echo "Setting the log4j configuration on the driver - done"
fi