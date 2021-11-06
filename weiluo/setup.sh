CUR_PATH=`pwd`

psql task1database < ${CUR_PATH}/ddl.sql
echo "Created tables"

psql task1database < ${CUR_PATH}/loaddata.sql
echo "Loaded data into tables"
