source my--credentials.sh

python ./train.py -u ${username}:${password} -i ../../data/v2/ground_truth.csv -c ${solr_cluster_id} -x watson_informer_collection -n "watson_informer_ranker"