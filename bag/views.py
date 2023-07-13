from django.shortcuts import render

def view_bag(request):
    #views whats in bag

    return render(request,'bag/bag.html')