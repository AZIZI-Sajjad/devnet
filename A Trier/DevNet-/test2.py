import dictdiffer                                          

a_dict = {                                              
  'a': '(002) Port1 Traffic',
  'b': '(006) Port7 Traffic',
  'c': '(005) Port5 Traffic',
  'd': '(007) ipsec Traffic',
  'e': '(010) Lo Traffic',

}                                                          

b_dict = {                                                 
  'Port7': 'WAN78LORAH2',                                              
  'Port1': 'LAN78LORAH2',
  'Port5': 'Port5',
  'Port8': 'Port8',
}                                                          

for diff in list(dictdiffer.diff(a_dict, b_dict)):         
    print (diff)