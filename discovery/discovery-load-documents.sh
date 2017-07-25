USERNAME=""
PASSWORD=""
API_BASE_URL="https://gateway.watsonplatform.net/discovery/api"
ENVIRONMENT_ID=""
COLLECTION_ID=""

#curl -X GET -u "${USERNAME}":"${PASSWORD}" "${API_BASE_URL}/v1/environments/${ENVIRONMENT_ID}/collections/${COLLECTION_ID}/documents?version=2017-06-25"

#echo "${API_BASE_URL}/v1/environments/${ENVIRONMENT_ID}/collections/${COLLECTION_ID}/documents?version=2017-06-25"

for file in ../data/posts/*
do	
  curl -X POST -u "${USERNAME}":"${PASSWORD}" -F file=@${file} "https://gateway.watsonplatform.net/discovery/api/v1/environments/${ENVIRONMENT_ID}/collections/${COLLECTION_ID}/documents?version=2017-06-25"

  #exit 1
done
