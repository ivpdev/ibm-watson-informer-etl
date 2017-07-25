source my--credentials.sh

curl -X POST -H "Content-Type: application/json" -u "${username}":"${password}" "https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/${solr_cluster_id}/solr/watson_informer_collection/update" --data-binary @../../data/v2/answers.json
