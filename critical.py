# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import Queue
INF = 10000000

class Critical:
	def __init__(self,v,V,edges):
		self.v = v
		self.edges = edges
		self.tplist = []

	# トポロジカルソート
	def topological_sort(self):
		visited = [False] * V
		tplist = []
		for i in range(V):
			if not visited[i]: self.trace(i,visited)
		self.tplist.reverse()
		print self.tplist

	def trace(self,v,visited):
		visited[v] = True
		for e in edges[v]:
			if visited[ e['to'] ]:
				continue
			self.trace(e['to'],visited)
		self.tplist.append(v)

	# トポロジカル順序で動的計画法
	def run(self,s):
		dp = [0] * V
		self.topological_sort()
		for v in self.tplist:
			for e in edges[v]:
				dp[e['to']] = max(dp[v]+e['weight'], dp[e['to']])
		print dp
		return dp

V,E = map(int,raw_input().split())
edges = [[] for i in range(V)]		#隣接リスト
edge_labels = {}	# 辺の描画用のラベル

g = nx.DiGraph()	#有向グラフの生成
for i in xrange(E):
	(a,b,w) = map(int,raw_input().split())
	g.add_edge(a,b,weight=w)
	edges[a].append({'to':b,'weight':w})
	edge_labels[(a,b)] = w

# critical path用のオブジェクト
cr = Critical(0,V,edges)
distance = cr.run(0)

labels = {}	# ノードの描画用のラベル
s = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(V):
	labels[i] =  s[i] #s[i] を distance[i]に変えれば,最長距離がノードのラベル


# 適当に表示
pos = nx.spring_layout(g)
nx.draw_networkx_nodes(g,pos,nodelist=g.nodes(),node_size=600)
nx.draw_networkx_edges(g,pos,edgelist=g.edges())
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels,font_size=12)
nx.draw_networkx_labels(g,pos,labels,font_size=20)
plt.axis('off')
plt.show()


