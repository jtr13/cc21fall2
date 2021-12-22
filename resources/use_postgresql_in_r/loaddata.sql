BEGIN;
COPY part FROM '/Users/lw/Desktop/STATGR5702/community/part.csv' WITH (FORMAT csv, DELIMITER '|');
COMMIT;