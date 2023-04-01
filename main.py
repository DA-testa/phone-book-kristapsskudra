# python3
# Kristaps Skudra 161REB074
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    # keep ansvers
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # if contact with same phone number alredy exist, otherwise its name
            contacts[cur_query.number] = cur_query.name
            # if we already have contact with such number,
            # we should rewrite contact's name
            
        elif cur_query.type == 'del':
            # if not in contacts - than skip
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            # if not in contacts than outprint- not found
            last = contacts.get(cur_query.number, 'not found')
            result.append(last)
    return result
        

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

