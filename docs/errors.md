<h1 align="center">Wesician Errors</h1>
<table>
  <tr>
    <th>Error code</th>
    <th>Base error</th>
    <th>Description</th>
    <th>Fix</th>
  </tr>
  <tr>
    <td>0x001</td>
    <td>json.decoder.JSONDecodeError</td>
    <td>Wesician can't find the JSON in your inputted HTTPCache file.  Please make sure that the file you inputted is JSON (Ignore the HTTP headers at the top, it ignores that).</td>
    <td>Make sure the HTTPCache file is JSON.</td>
  </tr>
  <tr>
    <td>0x002</td>
    <td>UnicodeDecodeError</td>
    <td>The input file is not ASCII text.  (Support for other types may be added later.)</td>
    <td>Use a different file.</td>
</table>
