from collections import defaultdict

def best_sender(messages, senders):
    sender_count = defaultdict(int)

    for i in range(len(messages)):
        sender_count[senders[i]] += len(messages[i].split())
    
    best = max(sender_count.items(), key=lambda x: (x[1], x[0]))
    return best[0]


messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))