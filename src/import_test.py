from fms import FileManager


class TemplateFactory:
    map_ = {}

    # 模块初始化
    @staticmethod
    def initialize():
        TemplateFactory.auto_register()

    # 生成custom_template文件夹下的指定模块
    @staticmethod
    def create_template(template_name):
        this_module = __import__(name='.'.join(['custom_template', template_name]), fromlist=[template_name, ])
        return this_module.Template()

    # 注册custom_template下的当前所有模块内的模板
    @staticmethod
    def auto_register():
        all_templates = FileManager.no_subdir_type_files('./custom_template', '.py')
        for template_name in all_templates:
            TemplateFactory.template_register(template_name)

    # 注册custom_template文件夹下的指定模块
    @staticmethod
    def template_register(template_name):
        try:
            TemplateFactory.map_[template_name] = TemplateFactory.create_template(template_name)
        except:
            print('模板注册失败！')

    # 根据模板名获取指定模板对象
    @staticmethod
    def get_template(template_name):
        return TemplateFactory.map_[template_name]



TemplateFactory.initialize()
cc = TemplateFactory.get_template('TestATemplate')
print(cc.say)
