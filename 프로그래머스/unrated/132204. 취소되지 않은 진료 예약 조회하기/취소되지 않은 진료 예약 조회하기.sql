select a.apnt_no, p.pt_name, p.pt_no, a.mcdp_cd, d.dr_name, a.apnt_ymd from appointment a inner join patient p on (a.pt_no = p.pt_no) inner join doctor d on (a.mddr_id = d.dr_id and d.mcdp_cd = 'CS')
where date_format(a.apnt_ymd,'%Y-%m-%d') = '2022-04-13' and a.apnt_cncl_yn = 'N'
order by a.apnt_ymd