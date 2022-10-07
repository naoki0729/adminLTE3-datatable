from django.shortcuts import render
from django.views.generic import ListView
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64




class MainView:
    
    # 棒グラフを出したい時
    # def dashboard_view(request): # ViewFunctionと呼ぶ
    #    chart_label = ['レッド', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
    #    chart_data = [1, 5, 1, 0, 0, 0]
    #    context = {'chart_data': chart_data, 'chart_label': chart_label}
    #    return render(request,template_name,context)
    
    # datatableを出したい時
    def datatable_view(request): # ViewFunctionと呼ぶ
        template_name = "main.html"
        ctx = {}
        ctx["object_list"] = [{'id':1, 'name':'北海道'},{'id':2, 'name':'青森県'},{'id':3, 'name':'岩手県'}]
        return render(request, template_name, ctx)

    # リストが機能しているか見たい時
    # def myapp_list_view(request):
    #     ctx = {}
    #     ctx["object_list"] = ["python", "javascript", "html", "css"]
    #     ctx["object_tuple"] = ("python", "javascript", "html", "css")
    #     ctx["object_dict"] = {"P": "python", "J": "javascript", "H": "html", "C": "css"}
    #     ctx["object_empty"] = []
    #     return render(request, template_name, ctx)

# class Dash2View(ListView):
#     template_name = "dashboard2.html"

# class Dash3View(ListView):
#     template_name = "dashboard3.html"

def Dash2_view(request):
    chart_label = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
    chart_data = [1, 5, 1, 0, 0, 0]
    context = {'chart_data': chart_data, 'chart_label': chart_label}
    return render(request, "dashboard2.html",context)


def create_graph(x_list,t_list):
    plt.cla()
    plt.plot(t_list, x_list, label="x")
    plt.xlabel('t')
    plt.ylabel('x')

def get_image():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def Dash3_view(request):
    x_list = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072]
    t_list = [1,2,3,4,5,6,7,8,9,10,11]
    create_graph(x_list, t_list)
    graph = get_image()
    return render(request, "dashboard3.html", {'graph': graph})