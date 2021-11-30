package mybatis;

import java.util.List;

import org.apache.ibatis.session.SqlSession;

public class EmpDAO {

	SqlSession session;
	public void setSqlSession(SqlSession session) {
		this.session = session;
	}
	public List<EmpVO> getEmpList(){
		//sql 정의 태그 중에서 id=emplist 실행-결과
		List<EmpVO> list = session.selectList("emp.emplist");
		return list;
	}
	public EmpVO getEmpOne(int id) {
		EmpVO vo = session.selectOne("emp.empone",id);
		return vo;
	}
	
	public void insertEmp(EmpVO vo) {
		session.insert("emp.insertemp", vo);
	}
	public void updateEmp(EmpVO vo) {
		session.update("emp.updateemp", vo);
	}
	public void deleteEmp(String name) {
		session.delete("emp.deleteemp",name);
	}
	public int countEmp() {
		int cnt = session.selectOne("emp.cnt");
		return cnt;
	}
	public empDeptList(int[] dept_list) {
		List<EmpVO> list  = session.selectList("emp.empdeptlist", dept_list);
		return list;
	}
}
