--- This is a script use for extracting the number of citations of patents of 16 LME CME countries.
--- The script is used for EPO PATSTAT databse, 2020 Spring Edition.

--- The script will give a table include the number of forward citation and backward citation of a patent
--- in  the 8 international patent classification (ipc) clasees. The patent we are looking for has to be 
--- granted, and the registered in bwtween 2000-2019, and is typical LMEs and CMEs.


--- The output will be used for the measuring the radicalty of innocations of a country as following. The method
--- is used according to 2009 Akkremans, et al.



--- Work for 2020 Yuzhou Liu's Paper,


--- Code by Jinhan Mei
--- 2020.08.08 @ Beijing




select 
	t1.appln_id, t4.st3_name, t1.earliest_filing_year, substring(t9.ipc_class_symbol, 1, 1),
	c.cited1, c.cited2, c.cited3, c.cited4, c.cited5, c.cited6, c.cited7, c.cited8,
	c.citing1, c.citing2, c.citing3, c.citing4, c.citing5, c.citing6, c.citing7, c.citing8
from
	tls201_appln t1, tls801_country t4, tls209_appln_ipc t9, tls211_pat_publn t11,

(select
b1.pat_publn_id,
sum(case b1.symbol when 'A' then b1.cited_number else 0 end) as cited1,
max(case b1.symbol when 'B' then b1.cited_number else 0 end)as cited2,
max(case b1.symbol when 'C' then b1.cited_number else 0 end)as cited3,
max(case b1.symbol when 'D' then b1.cited_number else 0 end)as cited4,
max(case b1.symbol when 'E' then b1.cited_number else 0 end)as cited5,
max(case b1.symbol when 'F' then b1.cited_number else 0 end)as cited6,
max(case b1.symbol when 'G' then b1.cited_number else 0 end)as cited7,
max(case b1.symbol when 'H' then b1.cited_number else 0 end)as cited8,

max(case b2.symbol when 'A' then b2.cited_number else 0 end)as citing1,
max(case b2.symbol when 'B' then b2.cited_number else 0 end)as citing2,
max(case b2.symbol when 'C' then b2.cited_number else 0 end)as citing3,
max(case b2.symbol when 'D' then b2.cited_number else 0 end)as citing4,
max(case b2.symbol when 'E' then b2.cited_number else 0 end)as citing5,
max(case b2.symbol when 'F' then b2.cited_number else 0 end)as citing6,
max(case b2.symbol when 'G' then b2.cited_number else 0 end)as citing7,
max(case b2.symbol when 'H' then b2.cited_number else 0 end)as citing8

from
(select
	a1.pat_publn_id, a1.symbol, count(a1.cited_pat_publn_id) as cited_number
from
	(select t3.pat_publn_id, t3.cited_pat_publn_id, substring(t9.ipc_class_symbol,1,1) as symbol 
		from 
			tls201_appln t1, tls212_citation t3,tls209_appln_ipc t9, tls211_pat_publn t11 
		where
				t11.appln_id = t1.appln_id
			and 
				t3.cited_pat_publn_id = t11.pat_publn_id 
			and 
				t1.appln_id = t9.appln_id ) 
	as a1 
group by a1.pat_publn_id, a1.symbol ) as b1,

(select
	a2.pat_publn_id, a2.symbol,count(a2.cited_pat_publn_id) as cited_number
from
	(select t3.pat_publn_id, t3.cited_pat_publn_id, substring(t9.ipc_class_symbol,1,1) as symbol 
		from 
			tls201_appln t1, tls212_citation t3,tls209_appln_ipc t9, tls211_pat_publn t11 
		where
				t11.appln_id = t1.appln_id
			and 
				t3.pat_publn_id = t11.pat_publn_id 
			and 
				t1.appln_id = t9.appln_id) 
	as a2
 group by a2.pat_publn_id, a2.symbol) as b2
 
 where 
	b1.pat_publn_id = b2.pat_publn_id
group by 
	b1.pat_publn_id) as c

where
		t1.appln_auth = t4.ctry_code
	and
		t1.appln_id = t9.appln_id
	and 
		t1.granted = 'Y'
	and 
		(t1.earliest_filing_year between 2000 and 2019)
	and 
		t1.appln_auth in ('AT', 'AU', 'BE', 'CA', 'CH', 'DE', 'DK', 'FI', 'GB', 'IE', 'JP', 'NL', 'NO', 'NZ', 'SE', 'US')
    and
    	t1.appln_id = t11.appln_id
    and
    	t11.pat_publn_id = c.pat_publn_id

group by
	t1.appln_id, t4.st3_name, t1.earliest_filing_year, substring(t9.ipc_class_symbol, 1, 1), c.cited1, c.cited2, c.cited3,
	c.cited4, c.cited5, c.cited6, c.cited7, c.cited8, c.citing1, c.citing2, c.citing3, c.citing4, c.citing5, c.citing6,
	c.citing7, c.citing8