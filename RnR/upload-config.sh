source my--credentials.sh

curl -X POST -H "Content-Type: application/zip" -u "${username}":"${password}" "https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/${solr_cluster_id}/config/watson_informer_config" --data-binary @SO-solr-config/SO-solr-config.zip
