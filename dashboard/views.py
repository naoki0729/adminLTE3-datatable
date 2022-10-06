from django.shortcuts import render
from django.views.generic import ListView




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
    chart_label = ['レッド', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
    chart_data = [1, 5, 1, 0, 0, 0]
    context = {'chart_data': chart_data, 'chart_label': chart_label}
    return render(request, "dashboard2.html",context)

def Dash3_view(request):
    
    return render(request, "dashboard3.html")