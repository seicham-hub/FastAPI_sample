export TBLS_VERSION=1.74.0
curl -o tbls.deb -L https://github.com/k1LoW/tbls/releases/download/v$TBLS_VERSION/tbls_$TBLS_VERSION-1_amd64.deb
dpkg -i tbls.deb

cat << EOM > .tbls.yml
# .tbls.yml

# DSN (Database Source Name) to connect database
dsn: postgres://dbuser:dbpass@localhost:5432/dbname

# Path to generate document
# Default is 'dbdoc'
docPath: er_diagram/doc/schema
EOM