# coding:utf-8

class Asset(object):
    """모든 asset의 기본이 되는 class 입니다.
    
    """
    def __inti__(self, root, thumbnail, history, project, uuid, assetType=None):
        self.root      = root
        self.thumbnail = thumbnail
        self.history   = history
        self.project   = project
        self.uuid      = uuid
        self.assetType = assetType
        