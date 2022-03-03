#!/bin/sh
old="coverage_old.json"
new="coverage_new.json"

# Create old file if it does not exist
if ! [ -f $old ]; then
    echo ""
    cp $new $old
fi

# Compare coverage
python compare_coverage.py $old $new

error=$?

# Overwrite old with new if coverage did not decrease
if [ $error -eq 0 ]; then
    cp $new $old
fi

exit $error
