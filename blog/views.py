from django.shortcuts import render, HttpResponse

# Create your views here.
def list(request):
    post_list = [
        {
            "id":1,
            "title": "Bread Basket",
            "summary":"Assortment of fresh baked fruit breads and muffins 5.50"
        },
        {
            "id":2,
            "title": "Honey Almond Granola with Fruits",
            "summary":"Natural cereal of honey toasted oats, raisins, almonds and dates 7.00"
        },
        {
             "id":3,
            "title": "Belgian Waffle",
            "summary":"Vanilla flavored batter with malted flour 7.50"
        },
        {
             "id":4,
            "title": "Scrambled eggs",
            "summary":"Scrambled eggs, roasted red pepper and garlic, with green onions 7.50"
        },
         {
            "id":5,
            "title": "Blueberry Pancakes",
            "summary":"With syrup, butter and lots of berries 8.50"
        }
    ]
    context = {
        "post_list":post_list
    }
    return render(request, "blog/list.html", context)
def detail(request, id):
    context = {
        "title": f"POST DETAIL {id}",
        "content": f'''<h4>Bread Basket {id}</h4>
                <p class="w3-text-grey">Assortment of fresh baked fruit breads and muffins 5.50</p><br>
            
                <h4>Honey Almond Granola with Fruits</h4>
                <p class="w3-text-grey">Natural cereal of honey toasted oats, raisins, almonds and dates 7.00</p><br>
            
                <h4>Belgian Waffle</h4>
                <p class="w3-text-grey">Vanilla flavored batter with malted flour 7.50</p><br>
            
                <h4>Scrambled eggs</h4>
                <p class="w3-text-grey">Scrambled eggs, roasted red pepper and garlic, with green onions 7.50</p><br>
            
                <h4>Blueberry Pancakes</h4>
                <p class="w3-text-grey">With syrup, butter and lots of berries 8.50</p>'''
    }
    return render(request, "blog/detail.html", context)