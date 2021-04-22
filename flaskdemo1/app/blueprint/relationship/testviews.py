from flask import request, render_template

from . import relationship  # 蓝图引用进来
from ..user import login_required
from ...dataFun.relationship import personRelationship as data

@relationship.route('/test')
@login_required
def test():
    relName=data.getrel()
    nodeType= data.getnodeType()
    return render_template('relationship/test.html',relName=relName,nodeType=nodeType)