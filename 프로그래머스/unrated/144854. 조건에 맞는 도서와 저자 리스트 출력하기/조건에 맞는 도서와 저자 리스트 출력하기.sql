-- 코드를 입력하세요
SELECT b.book_id, a.author_name, to_char(published_date, 'yyyy-mm-dd') as published_date from book b inner join author a on (a.author_id = b.author_id)
where b.category in ('경제')
order by published_date