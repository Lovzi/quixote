# ## 1
#
#
#
#
# ## 2
#
# dp = [0 for i in range(1000)]
#
# with open('input.txt', 'r') as f:
#     data = f.readlines()
#
# data = map(lambda x: int(x), data)
#
# for d in data:
#     dp[d // 100] += 1
#
# start = 0
# end = 99
# for i in range(0, 1000):
#    print('%s-%s-%s' % (start+i*100, end+i*100, dp[i]))
#
# ## 3
#
# # with open('domain.txt', 'r') as f:
# #     domains = sorted(map(lambda x:x[2:], f.readlines()),
# #                      key=len, reverse=True)
# #
# #
# # def check():
#
#
# ### 4
# #
# # import math
# #
# # with open('input.txt', 'r') as f:
# #     data = [l.split() for l in f.readlines()]
# #
# #
# # def parse(data):
# #     tmp = {}
# #     for d in data:
# #         tmp.setdefault(d[0], {})
# #         tmp[d[0]]['count'] = tmp[d[0]].get('count', 0) + 1
# #         tmp[d[0]][d[1]] = tmp[d[0]].get(d[2], 0) + 1
# #
# #     def compute(single):
# #         yu = 0
# #         for k in single:
# #             yu += single[k] / single['count'] * math.log(single[k] / single['count'],2)
# #         return -yu
# #
# #     result = []
# #     for t in tmp:
# #         print(t, compute(tmp[t]))
# #
# # parse(data)
#
# def check(data, schema):
#     if isinstance(data, str) and schema == 'string':
#         return True
#     if isinstance(data, int) and schema == 'long':
#         return True
#     print(type(data), schema)
#     return False
#
#
# def type_check(data, schema):
#     result = True
#     if isinstance(data, dict):
#         for k in data:
#             result = result and type_check(data[k], schema[k])
#     elif isinstance(data, list):
#         for i, v in enumerate(data):
#             result = result and type_check(data[i], schema[0])
#     else:
#         result = result and check(data, schema)
#     return result
#
# schema = {
#         "organization":"string",
#         "type":"string",
#         "features":{
#             "timestamp":"long",
#             "cities":["string"],
#             "apps":[{"name":"string", "date":"string"}]
#         }
# }
#
# data = {
#     "organization":"shumei",
#     "type": "tech",
#     "features":{
#         "timestamp": '1558031759',
#          "cities":["BeiJing","ShangHai","ShenZhen"],
#          "apps":[
#              {"name":"TianWang", "date":"2018-01"},
#              {"name":"TianJing", "date":"2016-01"}]
#     }
# }






