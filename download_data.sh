DIR="Dataset/NATO"
FILE="5.+Battery+Data+Set.zip"
URL="https://phm-datasets.s3.amazonaws.com/NASA"

# Modern Bash method
if [[ -d "$DIR" ]]; then
    echo "$DIR exists."
else
    echo "$DIR does not exist."
    mkdir -p "$DIR"
fi

if [[ -f "$DIR/$FILE" ]]; then
    echo "$FILE exists."
else
    echo "$FILE does not exist. Downloading from $URL"
    wget -P "$DIR" "$URL/$FILE"
fi

unzip "$DIR/$FILE" -d "$DIR/"


