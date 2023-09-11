import FortigateApi3 as FortigateApi

fg = FortigateApi.Fortigate('192.168.60.162', 'root', 'admin', 'Test123')

fg.AddFwAddress('srv-A', '10.1.1.1/32')


fg.GetFwAddress('srv-A')

fg.SetFwAddress('srv-A', '10.2.2.2/32')

fg.DelFwAddress('srv-A')
