class DSU:
    def __init__(self, n: int) -> None:
        self.par = [i for i in range(n)]
        self.size = [1] * (n + 1)

    def find(self, node: int) -> int:
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]
    
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.size[p1] > self.size[p2]:
            self.size[p1] += self.size[p2]
            self.par[p2] = p1
        else:
            self.size[p2] += self.size[p1]
            self.par[p1] = p2
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        email_to_acc_i = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_acc_i:
                    dsu.union(i, email_to_acc_i[email])
                else:
                    email_to_acc_i[email] = i
        
        acc_leader_i_emails_group = defaultdict(list)
        for email, i in email_to_acc_i.items():
            leader = dsu.find(i)
            acc_leader_i_emails_group[leader].append(email)
        
        res = []
        for leader_i, emails in acc_leader_i_emails_group.items():
            name, *_ = accounts[leader_i]
            res.append([name, *sorted(emails)])
        return res
        

