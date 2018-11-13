#!/usr/bin/env python2
import psycopg2

top_articals = '  What are the most popular three articles of all time?'
top_articals1 = """
select title, count(*) as views from articles inner join
log on concat('/article/', articles.slug) = log.path
where log.status like '%200%'
group by log.path, articles.title order by views desc limit 3;
"""

top_authors = '  Who are the most popular article authors of all time?'
top_authors1 = """
select authors.name, count(*) as views from articles inner join
authors on articles.author = authors.id inner join
log on concat('/article/', articles.slug) = log.path where
log.status like '%200%' group by authors.name order by views desc
"""

error = '  On which days did more than 1% of requests lead to errors?'
error1 = """
select * from (
    select a.day,
    round(cast((100*b.hits) as numeric) / cast(a.hits as numeric), 2)
    as errp from
        (select date(time) as day, count(*) as hits from log group by day) as a
        inner join
        (select date(time) as day, count(*) as hits from log where status
        like '%404%' group by day) as b
    on a.day = b.day)
as t where errp > 1.0;
"""


class reporting_tool(object):
    def __init__(self):
        try:
            self.db = psycopg2.connect('dbname=news')
            self.cursor = self.db.cursor()
        except Exception as e:
            print e

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def answer(self, ques, query, suffix='views'):
        query = query.replace('\n', ' ')
        result = self.execute_query(query)
        print ques
        for i in range(len(result)):
            print "\t", i + 1, '.', result[i][0], '--', result[i][1], suffix
    print ''

if __name__ == '__main__':
    questions = reporting_tool()
    questions.answer(top_articals, top_articals1)
    questions.answer(top_authors, top_authors1)
    questions.answer(error, error1, '% error')
