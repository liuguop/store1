dict={"地球":{"中国":
                {"北京":{"昌平":{"流沙河":{"老牛湾":"汉科软"}}}},
             "m78星云":
                {"光之城":{"光之陆":{"光之塔":{"78":"特例家"}}}}}}
aa=input("请输入您的地址")
if aa in dict.keys():
    bb=input("请输入您的地址")
    if bb in  dict[aa].keys() :# keys的键
        print("ok")
        cc = input('请输入你的地址：')
        if cc in dict[aa][bb].keys():
            print('ok')
            dd = input('请输入你的地址：')
            if dd in dict[aa][bb][cc].keys():
                print('ok')
                print(dict[aa][bb][cc].keys())
                ee = input('请输入你的地址：')
                if ee in dict[aa][bb][cc][dd].keys():
                    print('ok')
                    ff = input('请输入你的地址：')
                    if ff in dict[aa][bb][cc][dd][ee].keys():
                        print('ok')
                        print(dict[aa][bb][cc][dd][ee][ff])
