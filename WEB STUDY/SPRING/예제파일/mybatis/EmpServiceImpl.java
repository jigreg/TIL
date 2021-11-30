package mybatis;

import java.util.List;

//main /mvc === service(1개 기능 메소드) === dao (1개 sql 메소드)
public class EmpServiceImpl implements EmpService {

	EmpDAO dao;
	public void setDao(EmpDAO dao) {
		this.dao= dao;
	}
	@Override
	public List<EmpVO> getEmpList() {
		return dao.getEmpList();
	}

	@Override
	public EmpVO getEmpOne(int id) {
		return dao.getEmpOne(id);
	}
	@Override
	public void insertEmp(EmpVO vo) {
		EmpVO RESULT = dao.getEmpOne(vo.getEmployee_id());
		if(RESULT == null) { dao.insertEmp(vo); }
	}
	@Override
	public void updateEmp(EmpVO vo) {
		dao.updateEmp(vo);
		
	}
	@Override
	public void deleteEmp(String name) {
		name = "%" + name + "%";
		dao.deleteEmp(name);
		
	}
	@Override
	public int countEmp() {
		return dao.countEmp();
	}
	@Override
	public List<EmpVO> empDeptList(int[] a) {
		// TODO Auto-generated method stub
		return empDeptList(a);
	}
	
	
	
	
	
	

}
