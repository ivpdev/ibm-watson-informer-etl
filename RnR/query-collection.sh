source my--credentials.sh

curl -X GET -u "${username}":"${password}" "https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/${solr_cluster_id}/solr/watson_informer_collection/select?q=watson" 