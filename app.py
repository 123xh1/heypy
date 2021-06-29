
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
    'name': '何岳静',
    'address' : '湖北荆州',
    'school':'湖北师范大学',
    'job': '软件设计师',
    'tel': '15355132454',
    'email': '64656738@qq.com',
    'description' : '忠实诚信,讲原则，说到做到，决不推卸责任；有自制力，做事情始终坚持有始有终，从不半途而废；会用100%的热情和精力投入到工作中；平易近人。为人诚恳,性格开朗,积极进取,适应力强、勤奋好学、脚踏实地，有较强的团队精神,工作积极进取,态度认真。',
    'social_media' : [
        {
            'link': 'https://www.facebook.com/nono',
            'icon' : 'fa-facebook-f'
        },
        {
            'link': 'https://github.com/nono',
            'icon' : 'fa-github'
        },
        {
            'link': 'linkedin.com/in/nono',
            'icon' : 'fa-linkedin-in'
        },
        {
            'link': 'https://twitter.com/nono',
            'icon' : 'fa-twitter'
        }
    ],
    'img': 'img/img_nono.jpg',
    'experiences' : [
        {
            'description' : '小学',
            'timeframe' : '2006 - 2012'
        },
        {
            'description' : '初中',
            'timeframe' : '2012 - 2015'
        },
        {
            'description' : '高中',
            'timeframe' : '2015 - 2018'
        },
        {
            'description' : '大学',          
            'timeframe' : '2018 - 2022'
        }
    ],
    'education' : [
        {
            'description' : '基于C语言的教务管理系统',
            'mention' : '指导老师：柯xx',
            'timeframe' : '2018 - 2019'
        },
        {
            'description' : '基于Java的飞机购票系统',
            'mention' : '指导老师：杨xx',
            'timeframe' : '2019-2020'
        },
        {
            'description' : '基于python的网页爬取',
            'mention' : '指导老师：李xx',
            'timeframe' : '2019-2020'
        },
        {
            'description' : '基于pygame的飞机大战小游戏',
            'mention' : '指导老师：李xx',
            'timeframe' : '2020 - 2021'
        }
    ],
    'programming_languages' : {
        'HMTL' : ['fa-html5', '100'], 
        'CSS' : ['fa-css3-alt', '100'], 
        'SASS' : ['fa-sass', '90'], 
        'JS' : ['fa-js-square', '90'],
        'Wordpress' : ['fa-wordpress', '80'],
        'Python': ['fa-python', '70'],
        'Mongo DB' : ['fa-database', '60'],
        'MySQL' : ['fa-database', '60'],
        'NodeJS' : ['fa-node-js', '50']
    },
    'languages' : {'French' : 'Native', 'English' : 'Professional', 'Spanish' : 'Professional', 'Italian' : 'Limited Working Proficiency'},
    'interests' : ['Dance', 'Travel', 'Languages']
}

@app.route('/')
def cv(person=person):
    return render_template('index2.html', person=person)




@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return gm(request.args.get('data'))
   
@app.route('/chart')
def index():
	return render_template('chartsajax.html',  graphJSON1=gm1(),graphJSON2=gm2(),graphJSON3=gm3(),graphJSON4=gm4(),graphJSON5=gm5(),graphJSON6=gm6(),graphJSON7=gm7(),graphJSON8=gm8(),graphJSON9=gm9())

def gm1(borough='Brent'):
	df = pd.read_csv('./london_murders.csv',encoding="gbk")

	fig1 = px.line(df[df['borough']==borough], x="date", y="age")

	graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON1
    
def gm2():
    df = pd.read_csv('./london_murders.csv',encoding="gbk")

    fig2 = px.histogram(df,x="borough", y="age",color='year')

    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON2
def gm3():
    df = pd.read_csv('./london_murders.csv',encoding="gbk")

    fig3 = px.scatter(df,x="date", y="age",color='borough')

    graphJSON3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON3
def gm4():
    df = pd.read_csv('./london_murders.csv',encoding="gbk")

    fig4 = px.density_contour(df,x="date", y="age")

    graphJSON4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON4
def gm5():
    df = pd.read_csv('./london_murders.csv',encoding="gbk")

    fig5 = px.box(df,x="borough", y="age",color="year", notched=True)

    graphJSON5 = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON5
def gm6():
    df = pd.read_csv('./london_murders.csv',encoding="gbk")

    fig6 = px.violin(df,x="borough", y="age",color="year",box=True, points="all", 
          hover_data=df.columns)
    graphJSON6 = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON6
def gm7():
    df = pd.read_csv('./london_murders.csv',encoding="gbk")

    fig7 = px.parallel_categories(df,color="year", color_continuous_scale=px.
            colors.sequential.Inferno)
    graphJSON7 = json.dumps(fig7, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON7
def gm8():
    df = pd.read_csv('./london_murders.csv',encoding="gbk")

    fig8 = px.area(df, x="borough", y="age", color="year", 
        line_group="date")
    graphJSON8 = json.dumps(fig8, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON8
def gm9():
    df = pd.read_csv('./london_murders.csv',encoding="gbk")
    fig9 = px.pie(df,  values="age",names="year")
    graphJSON9 = json.dumps(fig9, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON9
@app.route('/senti')
def main():
	text = ""
	values = {"positive": 0, "negative": 0, "neutral": 0}

	with open('ask_politics.csv', 'rt') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		for idx, row in enumerate(reader):
			if idx > 0 and idx % 2000 == 0:
				break
			if  'text' in row:
				nolinkstext = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', row['text'], flags=re.MULTILINE)
				text = nolinkstext

			blob = TextBlob(text)
			for sentence in blob.sentences:
				sentiment_value = sentence.sentiment.polarity
				if sentiment_value >= -0.1 and sentiment_value <= 0.1:
					values['neutral'] += 1
				elif sentiment_value < 0:
					values['negative'] += 1
				elif sentiment_value > 0:
					values['positive'] += 1

	values = sorted(values.items(), key=operator.itemgetter(1))
	top_ten = list(reversed(values))
	if len(top_ten) >= 11:
		top_ten = top_ten[1:11]
	else :
		top_ten = top_ten[0:len(top_ten)]

	top_ten_list_vals = []
	top_ten_list_labels = []
	for language in top_ten:
		top_ten_list_vals.append(language[1])
		top_ten_list_labels.append(language[0])

	graph_values = [{
					'labels': top_ten_list_labels,
					'values': top_ten_list_vals,
					'type': 'pie',
					'insidetextfont': {'color': '#FFFFFF',
										'size': '14',
										},
					'textfont': {'color': '#FFFFFF',
										'size': '14',
								},
					}]

	layout = {'title': '<b>意见挖掘</b>'}

	return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
