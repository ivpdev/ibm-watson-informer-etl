source my--credentials.sh

curl -X POST -u "${username}":"${password}" "https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/${solr_cluster_id}/solr/admin/collections" -d "action=CREATE&name=watson_informer_collection&collection.configName=watson_informer_config"