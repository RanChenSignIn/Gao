"""
        #获取同一电极诚实与说谎的数据最大值，
        hon_max=mean_hon.max()
        ly_max=mean_lying.max()
        if hon_max>ly_max:
            mean_max=hon_max
        else:
            mean_max=ly_max
        #获取同一电极诚实与说谎的数据最小值，
        hon_min=mean_hon.min()
        ly_min=mean_lying.min()
        if hon_min<ly_min:
            mean_min=hon_min
        else:
            mean_min=ly_min
        """