from GraphUtils import Graph


def get_ids_with_topic_input():
    s = input('Plz input the topic you want to search: ')
    candidates = Graph.search_terms(s)
    if not candidates:
        print('Nothing found')
    print('Do you mean:')
    for i in range(len(candidates)):
        print(i, candidates[i])
    chosen_one = int(input('Plz input the chosen one: '))
    docs = Graph.get_docs_by_term(candidates[chosen_one])
    print('We got these docs:')
    for doc in docs:
        print(doc)


get_ids_with_topic_input()
