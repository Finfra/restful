#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
print( "Content-Type: text/html")
print()

form = cgi.FieldStorage()

dan = form.getvalue('dan')
dan = int(dan) if dan else 0
print( "<html>")
print( '''<head><meta charset="utf-8" /></head>''')
print( "<body border=1>")
print( "<h1>%d 단 </h1>"% dan)
print( "    <table>")
for x in range(1,10):
    print( "        <tr>")
    print( "            <td>%d</td><td>X</td><td>%d</td><td>=</td><td>%d</td>"%(dan,x,x*dan))
    print( "        </tr>")
print( "    </table>")
print('<button onclick="goBack()">뒤로 가기</button>')
print('''
<script>
function goBack() {
  window.history.back();
}
</script>
''')

print( "</body>")
print( "</html>")

