import random
import string

def createList(n, range_L):
    """
        Accepts:
            n(Integer): length of list to be created
            range_L(Integer): A range from which values will be picked in the list

        Returns:
            L: A list of integers
    """
    L = []

    for i in range(n):
        elem = int(random.random() * range_L)
        L.append(elem)

    return L

def createStringList(n):
    """
        Accepts:
            n(Integer): length of list to be created
    
        Returns:
            L: A list of strings
    """ 

    lorem_text = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vitae magna elementum, finibus augue non, hendrerit sem. Integer sed faucibus nulla. Integer gravida, enim at placerat venenatis, quam dui dictum odio, nec tincidunt magna odio vitae sapien. Nulla volutpat malesuada lectus, ac convallis quam tincidunt eu. Nam eget lorem nec lorem bibendum venenatis id in lorem. Fusce interdum semper nibh vitae egestas. Aliquam rhoncus turpis blandit quam accumsan, laoreet dignissim metus dictum. Ut aliquam blandit dapibus. Morbi dignissim lorem eget erat volutpat rutrum. Phasellus hendrerit ex urna, ac tincidunt justo interdum viverra. Mauris semper malesuada libero vitae aliquam. Cras est felis, commodo venenatis ultricies id, aliquam a enim. Sed euismod neque ac nunc dictum blandit. Fusce consequat mauris vitae blandit pellentesque. Nam at pulvinar turpis. Quisque interdum in dolor in porttitor.

        Sed facilisis justo velit, nec tempor enim mattis nec. Sed mollis ante ac suscipit cursus. Maecenas venenatis lacus in ante eleifend, vel porttitor dolor accumsan. Etiam faucibus tortor a diam vestibulum, id rhoncus urna dapibus. Nunc leo mi, ultricies et lorem a, tristique tempor sem. Duis eget quam non erat posuere ornare. Mauris vel odio et nibh tempus aliquam. Integer sodales vel mauris vel malesuada. Phasellus porta metus quis tellus dictum, vel vehicula enim interdum. Vestibulum at sem sollicitudin lectus semper luctus. Fusce massa enim, bibendum non porta in, congue ac orci. Quisque vehicula diam vel felis auctor rutrum. Etiam sodales tortor nec enim fermentum, quis malesuada ipsum mattis. Maecenas leo neque, consequat eget ultricies et, iaculis quis leo. Vestibulum in ipsum et tortor luctus varius. Integer scelerisque, ligula et congue vulputate, libero felis egestas sem, vel semper ipsum ligula nec orci.

        Integer ullamcorper ligula quam, non mollis nisl sodales quis. Quisque ornare ante sit amet justo aliquam, sit amet eleifend diam faucibus. Sed tristique dignissim tortor vitae lacinia. Nunc eget ullamcorper est. Vivamus laoreet, dui nec eleifend venenatis, eros nisi convallis justo, ornare eleifend erat elit vitae ipsum. Mauris viverra enim ipsum, a volutpat ex semper at. Maecenas porttitor velit faucibus dui pulvinar, ac tincidunt velit ullamcorper. Praesent vel libero ac justo finibus vestibulum vitae in leo. Proin hendrerit aliquet fermentum.

        Sed iaculis lorem sagittis ligula ultricies, ut vestibulum lorem laoreet. Vivamus sed semper augue, vehicula iaculis leo. Vivamus sollicitudin sed arcu vel laoreet. Nam sit amet justo non neque vestibulum blandit. Donec ut sem accumsan, accumsan velit id, blandit tortor. Aliquam ut dignissim quam. Sed sapien sem, molestie quis viverra ac, venenatis ut est. Pellentesque tristique arcu at purus sollicitudin, a tempor augue placerat. Aliquam erat volutpat. Phasellus eget ipsum ullamcorper, facilisis mi eget, vehicula dui. Donec placerat sit amet odio at volutpat. Nulla massa sem, semper ut rhoncus ac, mollis nec neque. Fusce convallis sodales leo, non mollis mauris luctus quis.

        Praesent rhoncus velit a neque pharetra congue. Suspendisse purus risus, molestie sit amet urna id, cursus lacinia lorem. Suspendisse hendrerit vestibulum massa. Ut augue sapien, aliquet nec enim nec, eleifend varius risus. Nulla tempor sem id ante scelerisque fringilla. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse potenti. Mauris pellentesque placerat odio eget ornare. Suspendisse auctor elementum diam, eu posuere justo tristique sed. Pellentesque dictum placerat quam at interdum. Ut nec enim tristique, efficitur lorem at, tempus nisl. Nulla sodales lectus sed mauris finibus gravida. Maecenas venenatis vestibulum imperdiet. Aenean malesuada facilisis odio id mattis. Pellentesque sit amet metus sem.
    """

    return lorem_text.split(' ')[ :n]