# Design and build accessible PDF tables
## Sample tables

Table 1

<table>
  <thead>
    <tr>
        <th>Column header (TH)</th>
        <th>Column header (TH)</th>
        <th>Column header (TH)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><strong>Row header (TH)</strong></td>
<td>Data cell (TD)</td>
<td>Data cell (TD)</td>
    </tr>
<tr>
        <td><strong>Row header(TH)</strong></td>
<td>Data cell (TD)</td>
<td>Data cell (TD)</td>
    </tr>
  </tbody>
</table>

Table 2: example of footnotes referenced from within a table

<table>
  <thead>
    <tr><th>Expenditure by function £ million</th><th>2009/10</th><th>2010/11<sup>1</sup></th></tr>
  </thead>
  <tbody>
    <tr>
        <td rowspan="3"><strong>Policy functions</strong></td>
<td><strong>Financial</strong></td>
<td>22.5</td>
<td>30.57</td>
    </tr>
<tr>
        <td><strong>Information</strong><sup>2</sup></td>
<td>10.2</td>
<td>14.8</td>
    </tr>
<tr>
        <td><strong>Contingency</strong></td>
<td>2.6</td>
<td>1.2</td>
    </tr>
<tr>
        <td rowspan="4"><strong>Remunerated functions</strong></td>
<td><strong>Agency services</strong><sup>3</sup></td>
<td>44.7</td>
<td>35.91</td>
    </tr>
<tr>
        <td><strong>Payments</strong></td>
<td>22.41</td>
<td>19.88</td>
    </tr>
<tr>
        <td><strong>Banking</strong></td>
<td>22.90</td>
<td>44.23</td>
    </tr>
<tr>
        <td><strong>Other</strong></td>
<td>12.69</td>
<td>10.32</td>
    </tr>
  </tbody>
</table>

<sup>(1)</sup> Provisional total as of publication date.

<sup>(2)</sup> Costs associated with on-going information programmes.

<sup>(3)</sup> From the management accounts, net of recoveries, including interest charges.

Table 3: "film credits" style layout

<table>
  <tbody>
    <tr>
        <td><strong>Main character</strong></td>
<td>Daniel Radcliffe</td>
    </tr>
<tr>
        <td><strong>Sidekick 1</strong></td>
<td>Rupert Grint</td>
    </tr>
<tr>
        <td><strong>Sidekick 2</strong></td>
<td>Emma Watson</td>
    </tr>
<tr>
        <td><strong>Lovable ogre</strong></td>
<td>Robbie Coltrane</td>
    </tr>
<tr>
        <td><strong>Professor</strong></td>
<td>Maggie Smith</td>
    </tr>
<tr>
        <td><strong>Headmaster</strong></td>
<td>Richard Harris</td>
    </tr>
  </tbody>
</table>



---

**Table 4: table 3 with column headers added**

<table>
  <thead>
    <tr>
        <th>Role</th>
        <th>Actor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Main character</td>
<td>Daniel Radcliffe</td>
    </tr>
<tr>
        <td>Sidekick 1</td>
<td>Rupert Grint</td>
    </tr>
<tr>
        <td>Sidekick 2</td>
<td>Emma Watson</td>
    </tr>
<tr>
        <td>Lovable ogre</td>
<td>Robbie Coltrane</td>
    </tr>
<tr>
        <td>Professor</td>
<td>Maggie Smith</td>
    </tr>
<tr>
        <td>Headmaster</td>
<td>Richard Harris</td>
    </tr>
  </tbody>
</table>

**Table 5: year-end financial statement (£, thousands)**

<table>
  <thead>
    <tr>
      <th></th>
      <th>2010</th>
      <th>2009</th>
      <th>2008</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4">Non-current assets</td>
    </tr>
<tr>
      <td>Property</td>
<td>345</td>
<td>445</td>
<td>222</td>
    </tr>
<tr>
      <td>Investment</td>
<td>567</td>
<td>654</td>
<td>423</td>
    </tr>
<tr>
      <td>Intangibles</td>
<td>423</td>
<td>123</td>
<td>453</td>
    </tr>
<tr>
      <td colspan="4">Current assets</td>
    </tr>
<tr>
      <td>Trade and other receivables</td>
<td>435</td>
<td>634</td>
<td>231</td>
    </tr>
<tr>
      <td>Cash and cash equivalents</td>
<td>524</td>
<td>123</td>
<td>482</td>
    </tr>
<tr>
      <td>Other</td>
<td>223</td>
<td>211</td>
<td>254</td>
    </tr>
  </tbody>
</table>

**Table 6: a table with a more serious headings problem**

<table>
  <thead>
    <tr>
      <th>Rainfall 
(inches)</th>
      <th>Americas</th>
      <th>Asia</th>
      <th>Europe</th>
      <th>Africa</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5">2010</td>
    </tr>
<tr>
      <td>Average</td>
<td>104</td>
<td>201</td>
<td>193</td>
<td>144</td>
    </tr>
<tr>
      <td>24 hour high</td>
<td>15</td>
<td>26</td>
<td>27</td>
<td>18</td>
    </tr>
<tr>
      <td>12 hour high</td>
<td>9</td>
<td>10</td>
<td>11</td>
<td>12</td>
    </tr>
<tr>
      <td colspan="5">2009</td>
    </tr>
<tr>
      <td>Average</td>
<td>133</td>
<td>244</td>
<td>155</td>
<td>166</td>
    </tr>
<tr>
      <td>24 hour high</td>
<td>27</td>
<td>28</td>
<td>29</td>
<td>20</td>
    </tr>
<tr>
      <td>12 hour high</td>
<td>11</td>
<td>12</td>
<td>13</td>
<td>16</td>
    </tr>
  </tbody>
</table>



---

**Table 7: year-end statement, non-current assets (£, thousands)**

<table>
  
  <tbody>
    <tr>
      <td>Non-current assets</td>
<td>2010</td>
<td>2009</td>
<td>2008</td>
    </tr>
<tr>
      <td>Property</td>
<td>345</td>
<td>445</td>
<td>222</td>
    </tr>
<tr>
      <td>Investment</td>
<td>567</td>
<td>654</td>
<td>423</td>
    </tr>
<tr>
      <td>Intangibles</td>
<td>423</td>
<td>123</td>
<td>453</td>
    </tr>
<tr>
      <td>Table 8: year-end statement, current assets</td>
<td></td>
<td>(£, thousands)</td>
<td></td>
    </tr>
<tr>
      <td>Current assets</td>
<td>2010</td>
<td>2009</td>
<td>2008</td>
    </tr>
<tr>
      <td>Trade and other receivables</td>
<td>435</td>
<td>634</td>
<td>231</td>
    </tr>
<tr>
      <td>Cash and cash equivalents</td>
<td>524</td>
<td>123</td>
<td>482</td>
    </tr>
<tr>
      <td>Other</td>
<td>223</td>
<td>211</td>
<td>254</td>
    </tr>
  </tbody>
</table>

**Table 9: rainfall by continent, 2009**

<table>
  <thead>
    <tr>
        <th>Rainfall (inches)</th>
        <th>Americas</th>
        <th>Asia</th>
        <th>Europe</th>
        <th>Africa</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Average</td>
<td>133</td>
<td>244</td>
<td>155</td>
<td>166</td>
    </tr>
<tr>
        <td>24 hour high</td>
<td>27</td>
<td>28</td>
<td>29</td>
<td>20</td>
    </tr>
<tr>
        <td>12 hour high</td>
<td>11</td>
<td>12</td>
<td>13</td>
<td>16</td>
    </tr>
  </tbody>
</table>



---

**Table 10: self-contained year-end statement (£, thousands) (multiple layout problems)**

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">2011</th>
      <th colspan="2">2010 restated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>General income</td>
<td></td>
<td>250,000</td>
<td></td>
<td>200,000</td>
    </tr>
<tr>
      <td>Increase in value, WIP</td>
<td></td>
<td>15,000</td>
<td></td>
<td>30,000</td>
    </tr>
<tr>
      <td></td>
<td></td>
<td>265,000</td>
<td></td>
<td>230,000</td>
    </tr>
<tr>
      <td colspan="5">Administrative costs</td>
    </tr>
<tr>
      <td>Staff costs</td>
<td>(200,000)</td>
<td></td>
<td>(150,000)</td>
<td></td>
    </tr>
<tr>
      <td>Early departures</td>
<td>(10,000)</td>
<td></td>
<td>(20,000)</td>
<td></td>
    </tr>
<tr>
      <td>Other</td>
<td>(25,000)</td>
<td></td>
<td>(10,000)</td>
<td></td>
    </tr>
<tr>
      <td>Depreciation</td>
<td>(10,000)</td>
<td></td>
<td>(10,000)</td>
<td></td>
    </tr>
<tr>
      <td colspan="5">Programme costs</td>
    </tr>
<tr>
      <td>Impairment loss</td>
<td>(10,000)</td>
<td></td>
<td>(5,000)</td>
<td></td>
    </tr>
<tr>
      <td>Other</td>
<td>(5,000)</td>
<td></td>
<td>(5,000)</td>
<td></td>
    </tr>
<tr>
      <td></td>
<td>(260,000)</td>
<td></td>
<td>(200,000)</td>
<td></td>
    </tr>
<tr>
      <td>Surplus</td>
<td></td>
<td>5,000</td>
<td></td>
<td>30,000</td>
    </tr>
  </tbody>
</table>

**Table 11: self-contained year-end statement (£, thousands) (multiple problems resolved)**

<table>
  <thead>
    <tr>
      <th></th>
      <th>2011</th>
      <th>2010 restated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>General income</td>
<td>250,000</td>
<td>200,000</td>
    </tr>
<tr>
      <td>Increase in value</td>
<td>15,000</td>
<td>30,000</td>
    </tr>
<tr>
      <td>Total income</td>
<td>265,000</td>
<td>230,000</td>
    </tr>
<tr>
      <td>Staff costs</td>
<td>(200,000)</td>
<td>(150,000)</td>
    </tr>
<tr>
      <td>Early departures</td>
<td>(10,000)</td>
<td>(20,000)</td>
    </tr>
<tr>
      <td>Other operating costs</td>
<td>(25,000)</td>
<td>(10,000)</td>
    </tr>
<tr>
      <td>Depreciation</td>
<td>(10,000)</td>
<td>(10,000)</td>
    </tr>
<tr>
      <td>Impairment loss</td>
<td>(10,000)</td>
<td>(5,000)</td>
    </tr>
<tr>
      <td>Other</td>
<td>(5,000)</td>
<td>(5,000)</td>
    </tr>
<tr>
      <td>Total costs</td>
<td>(260,000)</td>
<td>(200,000)</td>
    </tr>
<tr>
      <td>Surplus</td>
<td>5,000</td>
<td>30,000</td>
    </tr>
  </tbody>
</table>



---

**Table 12: merged data cells are not recommended**

<table>
  <thead>
    <tr>
        <th> </th>
        <th colspan="2">2008</th>
        <th colspan="2">2009</th>
    </tr>
<tr>
        <th><strong>Name</strong></th>
        <th><strong>Yes</strong></th>
        <th><strong>No</strong></th>
        <th><strong>Yes</strong></th>
        <th><strong>No</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><strong>Bob</strong></td>
<td>2</td>
<td>5</td>
<td>6</td>
<td>7</td>
    </tr>
<tr>
        <td><strong>Sue</strong></td>
<td>3</td>
<td>8</td>
<td>4</td>
<td>7</td>
    </tr>
<tr>
        <td><strong>Sam</strong></td>
        <td colspan="2">[data relating to both columns in<br/>a single cell spanning both]</td>
        <td colspan="2">[data relating to both columns in<br/>a single cell spanning both]</td>
    </tr>
  </tbody>
</table>

**Table 13: use of graphic symbols**

<table>
  <thead>
    <tr>
        <th><strong>Question</strong></th>
        <th><strong>Respondent A</strong></th>
        <th><strong>Respondent B</strong></th>
        <th><strong>Respondent C</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><strong>Are you a UK citizen?</strong></td>
<td>[yes]</td>
<td>[yes]</td>
<td>[yes]</td>
    </tr>
<tr>
        <td><strong>Are you currently employed?</strong></td>
<td>[yes]</td>
<td>[yes]</td>
<td>[yes]</td>
    </tr>
<tr>
        <td><strong>Do you have a driving licence?</strong></td>
<td>[yes]</td>
<td>[yes]</td>
<td>[yes]</td>
    </tr>
  </tbody>
</table>

**Table 14: symbols replaced by real text**

<table>
  <thead>
    <tr>
        <th><strong>Question</strong></th>
        <th><strong>Respondent A</strong></th>
        <th><strong>Respondent B</strong></th>
        <th><strong>Respondent C</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><strong>Are you a UK citizen?</strong></td>
<td>No</td>
<td>Yes</td>
<td>No</td>
    </tr>
<tr>
        <td><strong>Are you currently employed?</strong></td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
    </tr>
<tr>
        <td><strong>Do you have a driving licence?</strong></td>
<td>No</td>
<td>No</td>
<td>Yes</td>
    </tr>
  </tbody>
</table>

**Table 15: courses offered by Institution X. A = Bachelor of Science, B = Bachelor of Arts, C = Masters, D = Doctorate, E = Diploma**

<table>
  <thead>
    <tr>
        <th> </th>
        <th><strong>2006</strong></th>
        <th><strong>2007</strong></th>
        <th><strong>2008</strong></th>
        <th><strong>2009</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><strong>Economics</strong></td>
<td>A, B</td>
<td>A, C</td>
<td>A, B</td>
<td>A, C</td>
    </tr>
<tr>
        <td><strong>International relations</strong></td>
<td>A, E</td>
<td>A, E</td>
<td>A, B</td>
<td>A, E</td>
    </tr>
<tr>
        <td><strong>Philosophy</strong></td>
<td>A</td>
<td>A</td>
<td>A</td>
<td>A, D</td>
    </tr>
<tr>
        <td><strong>Politics</strong></td>
<td>A, D</td>
<td>A, D</td>
<td>A, D</td>
<td>A</td>
    </tr>
<tr>
        <td><strong>Mathematics</strong></td>
<td>B, C</td>
<td>B</td>
<td>A, E</td>
<td>A, B</td>
    </tr>
<tr>
        <td><strong>English</strong></td>
<td>A, C</td>
<td>A, B</td>
<td>A, B</td>
<td>C</td>
    </tr>
  </tbody>
</table>



---

**Table 16: Masters courses offered by Institution X**

<table>
  <thead>
    <tr>
        <th> </th>
        <th>2006</th>
        <th>2007</th>
        <th>2008</th>
        <th>2009</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><strong>Economics</strong></td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
    </tr>
<tr>
        <td><strong>International relations</strong></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
    </tr>
<tr>
        <td><strong>Philosophy</strong></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
    </tr>
<tr>
        <td><strong>Politics</strong></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
    </tr>
<tr>
        <td><strong>Mathematics</strong></td>
<td>Yes</td>
<td>No</td>
<td>No</td>
<td>No</td>
    </tr>
<tr>
        <td><strong>English</strong></td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
    </tr>
  </tbody>
</table>

**Table 17: accounts, 2011 (£, thousands)**

<table>
  <thead><tr><th>Accounting item</th><th>2011</th></tr></thead>
  <tbody>
    <tr>
      <td rowspan="3">Income</td>
<td>General income</td>
<td>200,000</td>
    </tr>
<tr>
      <td>Increase in value, WIP</td>
<td>30,000</td>
    </tr>
<tr>
      <td>Income subtotal</td>
<td>230,000</td>
    </tr>
<tr>
      <td rowspan="4">Administrative costs</td>
<td>Staff</td>
<td>150,000</td>
    </tr>
<tr>
      <td>Early departures</td>
<td>20,000</td>
    </tr>
<tr>
      <td>Other operating costs</td>
<td>10,000</td>
    </tr>
<tr>
      <td>Depreciation</td>
<td>10,000</td>
    </tr>
<tr>
      <td rowspan="2">Programme costs</td>
<td>Impairment loss</td>
<td>10,000</td>
    </tr>
<tr>
      <td>Costs subtotal</td>
<td>200,000</td>
    </tr>
<tr>
      <td colspan="2">Balance</td>
<td>30,000</td>
    </tr>
  </tbody>
</table>

**Table 18: accounts, 2011 (£, thousands)**

<table>
  <thead><tr><th>Accounting item</th><th>2011</th></tr></thead>
  <tbody>
    <tr>
      <td rowspan="3">Income</td>
<td>General income</td>
<td>200,000</td>
    </tr>
<tr>
      <td>Increase in value, WIP</td>
<td>30,000</td>
    </tr>
<tr>
      <td>Income subtotal</td>
<td>230,000</td>
    </tr>
<tr>
      <td rowspan="4">Administrative costs</td>
<td>Staff</td>
<td>(150,000)</td>
    </tr>
<tr>
      <td>Early departures</td>
<td>(20,000)</td>
    </tr>
<tr>
      <td>Other operating costs</td>
<td>(10,000)</td>
    </tr>
<tr>
      <td>Depreciation</td>
<td>(10,000)</td>
    </tr>
<tr>
      <td rowspan="2">Programme costs</td>
<td>Impairment loss</td>
<td>(10,000)</td>
    </tr>
<tr>
      <td>Costs subtotal</td>
<td>(200,000)</td>
    </tr>
<tr>
      <td colspan="2">Balance</td>
<td>30,000</td>
    </tr>
  </tbody>
</table>



---

**Table 19: Human Development Index (HDI) trends, 1980 to 2010. Source: Barro-Lee March, 2010**

<table>
  <thead>
    <tr>
        <th>Country</th>
        <th>1980</th>
        <th>1990</th>
        <th>2000</th>
        <th>2010</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><strong>Afghanistan</strong></td>
<td>0.78</td>
<td>1.48</td>
<td>2.16</td>
<td>3.33</td>
    </tr>
<tr>
        <td><strong>Albania</strong></td>
<td>8.89</td>
<td>9.67</td>
<td>9.89</td>
<td>10.38</td>
    </tr>
<tr>
        <td><strong>Algeria</strong></td>
<td>4.74</td>
<td>3.33</td>
<td>5.50</td>
<td>7.24</td>
    </tr>
<tr>
        <td><strong>Andorra</strong></td>
<td>4.98</td>
<td>5.63</td>
<td>9.09</td>
<td>10.35</td>
    </tr>
<tr>
        <td><strong>Angola</strong></td>
<td>-</td>
<td>-</td>
<td>4.42</td>
<td>4.42</td>
    </tr>
  </tbody>
</table>

**Table 20: footnotes referenced from within a table**

<table>
  <thead>
    <tr><th>Expenditure by function £million</th><th>2009/10</th><th>2010/11<sup>1</sup></th></tr>
  </thead>
  <tbody>
    <tr>
        <td rowspan="3"><strong>Policy functions</strong></td>
<td><strong>Financial</strong></td>
<td>22.5</td>
<td>30.57</td>
    </tr>
<tr>
        <td><strong>Information</strong><sup>2</sup></td>
<td>10.2</td>
<td>14.8</td>
    </tr>
<tr>
        <td><strong>Contingency</strong></td>
<td>2.6</td>
<td>1.2</td>
    </tr>
<tr>
        <td rowspan="4"><strong>Remunerated functions</strong></td>
<td><strong>Agency services</strong><sup>3</sup></td>
<td>44.7</td>
<td>35.91</td>
    </tr>
<tr>
        <td><strong>Payments</strong></td>
<td>22.41</td>
<td>19.88</td>
    </tr>
<tr>
        <td><strong>Banking</strong></td>
<td>22.90</td>
<td>44.23</td>
    </tr>
<tr>
        <td><strong>Other</strong></td>
<td>12.69</td>
<td>10.32</td>
    </tr>
  </tbody>
</table>

<sup>(1)</sup> Provisional total as of publication date.

<sup>(2)</sup> Costs associated with on-going information programmes.

<sup>(3)</sup> From the management accounts, net of recoveries and including interest charges

---

**Table 21: footnotes replaced by additional table summary text**

<table>
  
  <tbody>
    <tr>
      <td>Expenditure by function £million</td>
<td>2009/10</td>
<td>2010/11</td>
    </tr>
<tr>
      <td>Policy functions Financial</td>
<td>22.5</td>
<td>30.57</td>
    </tr>
<tr>
      <td>Information</td>
<td>10.2</td>
<td>14.8</td>
    </tr>
<tr>
      <td>Contingency</td>
<td>2.6</td>
<td>1.2</td>
    </tr>
<tr>
      <td>Remunerated functions Agency services</td>
<td>44.7</td>
<td>35.91</td>
    </tr>
<tr>
      <td>Payments</td>
<td>22.41</td>
<td>19.88</td>
    </tr>
<tr>
      <td>Banking</td>
<td>22.90</td>
<td>44.23</td>
    </tr>
<tr>
      <td>Other</td>
<td>12.69</td>
<td>10.32</td>
    </tr>
<tr>
      <td>Expenditure £m Notes</td>
<td>2010</td>
<td>2011</td>
    </tr>
<tr>
      <td>(Notes located on page [n])</td>
<td></td>
<td></td>
    </tr>
<tr>
      <td>Information 1</td>
<td>10.2</td>
<td>14.8</td>
    </tr>
<tr>
      <td>Contingency</td>
<td>2.6</td>
<td>1.2</td>
    </tr>
<tr>
      <td>Payments 3</td>
<td>22.41</td>
<td>19.88</td>
    </tr>
<tr>
      <td>Banking services 4</td>
<td>22.90</td>
<td>44.23</td>
    </tr>
<tr>
      <td>Interest</td>
<td>0.23</td>
<td>0.10</td>
    </tr>
<tr>
      <td>Dividends 23</td>
<td>2.5</td>
<td>3.68</td>
    </tr>
<tr>
      <td>Other 9</td>
<td>12.69</td>
<td>10.32</td>
    </tr>
  </tbody>
</table>

**Table 23: simulated table created using tabs and containing no structure**

<table>
  <thead>
    <tr>
        <th> </th>
        <th colspan="2">2008</th>
        <th colspan="2">2009</th>
    </tr>
<tr>
        <th><strong>Name</strong></th>
        <th><strong>Entered</strong></th>
        <th><strong>Completed</strong></th>
        <th><strong>Entered</strong></th>
        <th><strong>Completed</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><strong>Bob</strong></td>
<td>22</td>
<td>21</td>
<td>20</td>
<td>19</td>
    </tr>
<tr>
        <td><strong>Sue</strong></td>
<td>44</td>
<td>12</td>
<td>12</td>
<td>10</td>
    </tr>
  </tbody>
</table>



---

**Table 24: year-end financial statement (£, thousands)**

<table>
  <thead>
    <tr>
      <th></th>
      <th>2010</th>
      <th>2009</th>
      <th>2008</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4">Non-current assets</td>
    </tr>
<tr>
      <td>Buildings</td>
<td>345</td>
<td>445</td>
<td>222</td>
    </tr>
<tr>
      <td>Investment</td>
<td>567</td>
<td>654</td>
<td>423</td>
    </tr>
<tr>
      <td>Intangibles</td>
<td>423</td>
<td>123</td>
<td>453</td>
    </tr>
<tr>
      <td colspan="4">Current assets</td>
    </tr>
<tr>
      <td>Trade</td>
<td>435</td>
<td>634</td>
<td>231</td>
    </tr>
<tr>
      <td>Cash</td>
<td>524</td>
<td>123</td>
<td>482</td>
    </tr>
<tr>
      <td>Other</td>
<td>223</td>
<td>211</td>
<td>254</td>
    </tr>
<tr>
      <td colspan="4">Current liabilities</td>
    </tr>
<tr>
      <td>Trade liabilities</td>
<td>154</td>
<td>125</td>
<td>421</td>
    </tr>
<tr>
      <td>Financial debt</td>
<td>231</td>
<td>474</td>
<td>572</td>
    </tr>
<tr>
      <td>Provisions</td>
<td>111</td>
<td>312</td>
<td>347</td>
    </tr>
  </tbody>
</table>

**Table 25: setting column and row scope via the tags panel**

<table>
  <thead>
    <tr>
        <th> </th>
        <th colspan="2">2008</th>
        <th colspan="2">2009</th>
    </tr>
<tr>
        <th>Name</th>
        <th>Entered</th>
        <th>Won</th>
        <th>Entered</th>
        <th>Won</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><strong>Bob</strong></td>
<td>22</td>
<td>21</td>
<td>20</td>
<td>19</td>
    </tr>
<tr>
        <td><strong>Sue</strong></td>
<td>44</td>
<td>12</td>
<td>12</td>
<td>10</td>
    </tr>
<tr>
        <td><strong>Sam</strong></td>
<td>16</td>
<td>4</td>
<td>45</td>
<td>30</td>
    </tr>
  </tbody>
</table>

**Table 26: courses offered by Institution X. A = Bachelor of Science, B = Bachelor of Arts, C = Masters, D = Doctorate, E = Diploma**

<table>
  <thead>
    <tr>
        <th> </th>
        <th>2006</th>
        <th>2007</th>
        <th>2008</th>
        <th>2009</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><strong>Economics</strong></td>
<td>A, B</td>
<td>A, C</td>
<td>A, C</td>
<td>A, C</td>
    </tr>
<tr>
        <td><strong>International relations</strong></td>
<td>A, E</td>
<td>A, E</td>
<td>A, B</td>
<td>A, B</td>
    </tr>
<tr>
        <td><strong>Philosophy</strong></td>
<td>A</td>
<td>A</td>
<td>A</td>
<td>A</td>
    </tr>
<tr>
        <td><strong>Politics</strong></td>
<td>A, D</td>
<td>A, D</td>
<td>A, B</td>
<td>A</td>
    </tr>
<tr>
        <td><strong>Mathematics</strong></td>
<td>B, C</td>
<td>B</td>
<td>A, B</td>
<td>A, B</td>
    </tr>
<tr>
        <td><strong>English</strong></td>
<td>A, C</td>
<td>A, B</td>
<td>A, B</td>
<td>A, C</td>
    </tr>
  </tbody>
</table>



---

**Table 27: “table” with columns simulated by using tab stops**

<table>
  <thead>
    <tr>
        <th>Name</th>
        <th>Apples</th>
        <th>Pears</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><strong>Bob Scott</strong></td>
<td>20</td>
<td>25</td>
    </tr>
<tr>
        <td><strong>Susan. P. Arnold-Jones, BA, FRSA, MD</strong></td>
<td>24</td>
<td>15</td>
    </tr>
<tr>
        <td><strong>Sam Holder-Dickinson</strong></td>
<td>14</td>
<td>10</td>
    </tr>
  </tbody>
</table>

**Table 28: year-end financial table (£, thousands) – headings problem revisited**

<table>
  <thead>
    <tr>
      <th></th>
      <th>2010</th>
      <th>2009</th>
      <th>2008</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4">Non-current assets</td>
    </tr>
<tr>
      <td>Buildings</td>
<td>345</td>
<td>445</td>
<td>222</td>
    </tr>
<tr>
      <td>Investment</td>
<td>567</td>
<td>654</td>
<td>423</td>
    </tr>
<tr>
      <td>Intangibles</td>
<td>423</td>
<td>123</td>
<td>453</td>
    </tr>
<tr>
      <td colspan="4">Current assets</td>
    </tr>
<tr>
      <td>Trade</td>
<td>435</td>
<td>634</td>
<td>231</td>
    </tr>
<tr>
      <td>Cash</td>
<td>524</td>
<td>123</td>
<td>482</td>
    </tr>
<tr>
      <td>Other</td>
<td>223</td>
<td>211</td>
<td>254</td>
    </tr>
<tr>
      <td colspan="4">Current liabilities</td>
    </tr>
<tr>
      <td>Trade liabilities</td>
<td>154</td>
<td>125</td>
<td>421</td>
    </tr>
<tr>
      <td>Financial debt</td>
<td>231</td>
<td>474</td>
<td>572</td>
    </tr>
<tr>
      <td>Provisions</td>
<td>111</td>
<td>312</td>
<td>347</td>
    </tr>
  </tbody>
</table>



---

## Table 29: multiple headers attributes for each data cell

<table>
  <thead>
    <tr>
      <th></th>
      <th>South America</th>
      <th>Asia</th>
      <th>Africa</th>
      <th>Australia</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5">2010</td>
    </tr>
<tr>
      <td>Highest average</td>
<td>523.6</td>
<td>467.4</td>
<td>405.0</td>
<td>340.5</td>
    </tr>
<tr>
      <td>Highest in 24 hours</td>
<td>73.1</td>
<td>54.1</td>
<td>27.2</td>
<td>66.3</td>
    </tr>
<tr>
      <td>Highest in 12 hours</td>
<td>42.4</td>
<td>30.1</td>
<td>15.9</td>
<td>40.3</td>
    </tr>
<tr>
      <td colspan="5">2009</td>
    </tr>
<tr>
      <td>Highest average</td>
<td>487.7</td>
<td>453.6</td>
<td>398.7</td>
<td>356</td>
    </tr>
<tr>
      <td>Highest in 24 hours</td>
<td>67.2</td>
<td>53.2</td>
<td>44.3</td>
<td>53.8</td>
    </tr>
<tr>
      <td>Highest in 12 hours</td>
<td>34.7</td>
<td>34.1</td>
<td>29.8</td>
<td>31.0</td>
    </tr>
<tr>
      <td colspan="5">2008</td>
    </tr>
<tr>
      <td>Highest average</td>
<td>496.7</td>
<td>444.3</td>
<td>502.1</td>
<td>399.6</td>
    </tr>
<tr>
      <td>Highest in 24 hours</td>
<td>44.2</td>
<td>56.7</td>
<td>32.1</td>
<td>63.2</td>
    </tr>
<tr>
      <td>Highest in 12 hours</td>
<td>30.1</td>
<td>32.7</td>
<td>21.9</td>
<td>40.2</td>
    </tr>
  </tbody>
</table>

