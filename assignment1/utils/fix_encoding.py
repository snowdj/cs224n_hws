# use python 2

path = "datasets/stanfordSentimentTreebank"
with open(path + "/datasetSentences_backup.txt", "r") as f:
    data = f.read()
    data = data.decode('utf-8').encode('latin1')
    
with open(path + "/datasetSentences.txt", "w") as f:
    f.write(data)