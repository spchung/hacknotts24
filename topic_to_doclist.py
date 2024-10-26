class Graph:
    def __init__(self):
        pass

    def topics_to_doclist(NLP_list: list):
        for tuple in NLP_list:
            topic = tuple[0]
            freq = tuple[1]
            for document in notion.document_list:
                if topic in document:
                    # add doc to graph






"""
1. For each tuple in the NLP_list input
    Assign values (topic, freq)
    create topic node
    for each document:
        if topic in document (can implement fuzzy search later):
            tie document ID node to topic node



"""

